import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NewsView from '../views/NewsView.vue'
import PlayersView from '../views/PlayersView.vue'
import MatchesView from '../views/MatchesView.vue'
import ContactView from '../views/ContactView.vue'
import GearView from '../views/GearView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView, meta: { title: '首页' } },
  { path: '/news', name: 'news', component: NewsView, meta: { title: '资讯' } },
  { path: '/players', name: 'players', component: PlayersView, meta: { title: '球员' } },
  { path: '/matches', name: 'matches', component: MatchesView, meta: { title: '比赛' } },
  { path: '/contact', name: 'contact', component: ContactView, meta: { title: '联系我们' } },
  { path: '/gear', name: 'gear', component: GearView, meta: { title: '装备' } },
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
