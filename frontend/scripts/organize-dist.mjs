import fs from 'node:fs'
import path from 'node:path'

const dist = path.resolve(process.env.DIST_DIR || 'dist')
const pagesDir = path.join(dist, 'pages')
const cssDir = path.join(dist, 'css')
const jsDir = path.join(dist, 'js')
const assetsDir = path.join(dist, 'assets')

for (const dir of [pagesDir, cssDir, jsDir]) {
  fs.mkdirSync(dir, { recursive: true })
}

for (const file of fs.readdirSync(dist)) {
  if (file.endsWith('.html')) {
    fs.renameSync(path.join(dist, file), path.join(pagesDir, file))
  }
}

if (fs.existsSync(assetsDir)) {
  for (const file of fs.readdirSync(assetsDir)) {
    const source = path.join(assetsDir, file)
    if (file.endsWith('.css')) {
      fs.renameSync(source, path.join(cssDir, file))
    } else if (file.endsWith('.js')) {
      fs.renameSync(source, path.join(jsDir, file))
    }
  }
  fs.rmSync(assetsDir, { recursive: true, force: true })
}

fs.rmSync(path.join(dist, 'media'), { recursive: true, force: true })

for (const file of fs.readdirSync(pagesDir)) {
  if (!file.endsWith('.html')) continue
  const filePath = path.join(pagesDir, file)
  let html = fs.readFileSync(filePath, 'utf8')
  html = html.replace(/href="([^"]*)assets\/([^"]+\.css)"/g, 'href="$1css/$2"')
  html = html.replace(/href="([^"]*)assets\/([^"]+\.js)"/g, 'href="$1js/$2"')
  html = html.replace(/src="([^"]*)assets\/([^"]+\.js)"/g, 'src="$1js/$2"')
  html = html.replace(/href="\/css\//g, 'href="css/')
  html = html.replace(/href="\/js\//g, 'href="js/')
  html = html.replace(/src="\/js\//g, 'src="js/')
  html = html.replace(/src="\/images\//g, 'src="images/')
  html = html.replace(/src="\/videos\//g, 'src="videos/')
  html = html.replace(/poster="\/images\//g, 'poster="images/')
  html = html.replace(/href="\/logo\.svg"/g, 'href="logo.svg"')
  html = html.replace(/src="\/logo\.svg"/g, 'src="logo.svg"')
  html = html.replace(/\s*crossorigin(?:="[^"]*")?/g, '')
  fs.writeFileSync(filePath, html)
}

const redirect = `<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="refresh" content="0; url=./pages/index.html" />
    <title>羽界</title>
  </head>
  <body>
    <p><a href="./pages/index.html">进入网站</a></p>
  </body>
</html>
`
fs.writeFileSync(path.join(dist, 'index.html'), redirect)

console.log('dist organized: pages/, css/, js/, images/, videos/')
