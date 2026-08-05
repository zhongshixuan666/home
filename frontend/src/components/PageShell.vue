<script setup>
import { media } from '../media'

defineProps({
  page: { type: Object, default: null },
})

const logo = media('logo.svg')

const navs = [
  { name: '首页', href: media('index.html') },
  { name: '资讯', href: media('news.html') },
  { name: '球员', href: media('players.html') },
  { name: '比赛', href: media('matches.html') },
  { name: '联系我们', href: media('contact.html') },
  { name: '装备', href: media('gear.html') },
]

const currentFile = (window.location.pathname.split('/').filter(Boolean).pop() || 'index.html').toLowerCase()

function isActive(href) {
  const file = href.split('/').filter(Boolean).pop() || 'index.html'
  return file.toLowerCase() === currentFile
}
</script>

<template>
  <div class="app">
    <header class="topbar">
      <div class="container topbar-inner">
        <a :href="media('index.html')" class="brand">
          <img :src="logo" alt="羽界" class="brand-logo" />
        </a>
        <nav class="nav">
          <a
            v-for="item in navs"
            :key="item.href"
            :href="item.href"
            class="nav-link"
            :class="{ active: isActive(item.href) }"
          >
            {{ item.name }}
          </a>
        </nav>
      </div>
    </header>

    <main>
      <slot />
      <component v-if="page" :is="page" />
    </main>

    <footer class="footer">
      <div class="container footer-inner">
        <div>
          <p class="footer-brand">羽界 · YUJIE</p>
          <p class="footer-desc">羽毛球中文资讯官网 · 以专业视角记录羽坛</p>
        </div>
        <div class="footer-nav">
          <a v-for="item in navs" :key="item.href" :href="item.href">{{ item.name }}</a>
        </div>
        <p class="footer-copy">© 2026 羽界编辑部 · 仅供学习演示</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.topbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(255, 255, 255, 0.96);
  border-bottom: 1px solid var(--line);
}

.topbar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 80px;
}

.brand {
  display: flex;
  align-items: center;
}

.brand-logo {
  height: 44px;
  width: auto;
  display: block;
}

.nav {
  display: flex;
  gap: 48px;
}

.nav-link {
  position: relative;
  font-size: 14px;
  letter-spacing: 0.22em;
  color: var(--text);
  padding: 10px 0;
}

.nav-link::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 1px;
  background: var(--gold);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s var(--ease-out);
}

.nav-link:hover {
  color: var(--paper);
}

.nav-link:hover::after,
.nav-link.active::after {
  transform: scaleX(1);
}

.nav-link.active {
  color: var(--gold);
}

.footer {
  border-top: 1px solid var(--line);
  background: var(--bg-soft);
  padding: 72px 0 56px;
}

.footer-inner {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 24px;
}

.footer-brand {
  font-family: var(--serif);
  font-size: 20px;
  color: var(--paper);
  letter-spacing: 0.2em;
}

.footer-desc {
  font-size: 13px;
  color: var(--muted);
  margin-top: 6px;
}

.footer-nav {
  display: flex;
  gap: 26px;
  font-size: 13px;
  color: var(--text);
}

.footer-nav a {
  transition: color 0.3s ease;
}

.footer-nav a:hover {
  color: var(--gold);
}

.footer-copy {
  grid-column: 1 / -1;
  margin-top: 28px;
  padding-top: 22px;
  border-top: 1px solid var(--line);
  font-size: 12px;
  color: var(--muted);
}

@media (max-width: 860px) {
  .topbar-inner {
    flex-direction: column;
    height: auto;
    padding: 16px 24px;
    gap: 12px;
  }
  .nav {
    gap: 22px;
  }
}
</style>
