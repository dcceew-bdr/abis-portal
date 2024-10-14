import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/profiles',
      name: 'profiles',
      component: () => import('../views/ProfilesView.vue')
    },
    {
      path: '/vocabs',
      name: 'vocabs',
      component: () => import('../views/VocabsView.vue')
    },
    {
      path: '/system',
      name: 'system',
      component: () => import('../views/SytemView.vue')
    }
  ]
})

export default router
