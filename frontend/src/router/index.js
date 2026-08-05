import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('../views/HomeView.vue'), meta: { title: '首页' } },
  { path: '/news', name: 'news', component: () => import('../views/NewsView.vue'), meta: { title: '资讯' } },
  { path: '/players', name: 'players', component: () => import('../views/PlayersView.vue'), meta: { title: '球员' } },
  { path: '/matches', name: 'matches', component: () => import('../views/MatchesView.vue'), meta: { title: '比赛' } },
  { path: '/contact', name: 'contact', component: () => import('../views/ContactView.vue'), meta: { title: '联系我们' } },
  { path: '/gear', name: 'gear', component: () => import('../views/GearView.vue'), meta: { title: '装备' } },
]

const router = createRouter({
  history:
    import.meta.env.VITE_HASH_ROUTER === '1'
      ? createWebHashHistory(import.meta.env.BASE_URL)
      : createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

router.afterEach((to) => {
  document.title = to.meta.title ? `${to.meta.title} · 羽界` : '羽界 · 羽毛球中文资讯官网'
})

export default router
