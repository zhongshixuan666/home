import { createApp } from 'vue'
import '../style.css'
import PageShell from '../components/PageShell.vue'

export function createPage(page) {
  createApp(PageShell, { page }).mount('#app')
}
