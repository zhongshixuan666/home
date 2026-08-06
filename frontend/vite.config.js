import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// 桌面素材目录：视频与图片
const MEDIA_ROOT = 'C:/Users/轩/Desktop'

const MIME = {
  '.mp4': 'video/mp4',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.jfif': 'image/jpeg',
  '.png': 'image/png',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
}

// 将 /videos 与 /images 映射到桌面素材目录，供开发与预览时直接访问
function serveDesktopMedia() {
  const handler = (req, res, next) => {
    let file = null
    const urlPath = decodeURIComponent(req.url.split('?')[0])
    let rel = null
    if (urlPath.startsWith('/videos/')) {
      rel = path.join('video', urlPath.slice('/videos/'.length))
    } else if (urlPath.startsWith('/images/')) {
      rel = path.join('imges', urlPath.slice('/images/'.length))
    }
    if (!rel) return next()

    file = path.resolve(MEDIA_ROOT, rel)
    const root = path.resolve(MEDIA_ROOT) + path.sep
    if (!file.startsWith(root)) {
      res.statusCode = 403
      return res.end('Forbidden')
    }

    fs.stat(file, (err, stat) => {
      if (err || !stat.isFile()) {
        return next()
      }
      const ext = path.extname(file).toLowerCase()
      res.setHeader('Content-Type', MIME[ext] || 'application/octet-stream')

      // 支持 Range，视频可拖拽进度
      const range = req.headers.range
      if (range) {
        const match = /bytes=(\d+)-(\d*)/.exec(range)
        const start = match ? Number(match[1]) : 0
        const end = match && match[2] ? Number(match[2]) : stat.size - 1
        res.statusCode = 206
        res.setHeader('Content-Range', `bytes ${start}-${end}/${stat.size}`)
        res.setHeader('Accept-Ranges', 'bytes')
        fs.createReadStream(file, { start, end }).pipe(res)
      } else {
        res.setHeader('Content-Length', stat.size)
        res.setHeader('Accept-Ranges', 'bytes')
        fs.createReadStream(file).pipe(res)
      }
    })
  }
  return {
    name: 'serve-desktop-media',
    configureServer(server) {
      server.middlewares.use(handler)
    },
    configurePreviewServer(server) {
      server.middlewares.use(handler)
    },
  }
}

function servePageAliases() {
  const aliases = {
    '/news': '/news.html',
    '/pages/news.html': '/news.html',
    '/players': '/players.html',
    '/pages/players.html': '/players.html',
    '/matches': '/matches.html',
    '/pages/matches.html': '/matches.html',
    '/contact': '/contact.html',
    '/pages/contact.html': '/contact.html',
    '/gear': '/gear.html',
    '/pages/gear.html': '/gear.html',
    '/pages/index.html': '/index.html',
  }
  const handler = (req, res, next) => {
    const urlPath = decodeURIComponent(req.url.split('?')[0])
    if (aliases[urlPath]) {
      req.url = req.url.replace(urlPath, aliases[urlPath])
    }
    next()
  }
  return {
    name: 'serve-page-aliases',
    configureServer(server) {
      server.middlewares.use(handler)
    },
    configurePreviewServer(server) {
      server.middlewares.use(handler)
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  base: process.env.VITE_BASE || '/',
  plugins: [vue(), servePageAliases(), serveDesktopMedia()],
  build: {
    rollupOptions: {
      input: {
        main: fileURLToPath(new URL('./index.html', import.meta.url)),
        news: fileURLToPath(new URL('./news.html', import.meta.url)),
        players: fileURLToPath(new URL('./players.html', import.meta.url)),
        matches: fileURLToPath(new URL('./matches.html', import.meta.url)),
        contact: fileURLToPath(new URL('./contact.html', import.meta.url)),
        gear: fileURLToPath(new URL('./gear.html', import.meta.url)),
        login: fileURLToPath(new URL('./login.html', import.meta.url)),
        register: fileURLToPath(new URL('./register.html', import.meta.url)),
      },
    },
  },
  server: {
    port: 5173,
    proxy: {
      // 将 /api 开头的请求转发到 Django 后端
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
})
