import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfilesView from '../views/ProfilesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => HomeView
    },
    {
      path: '/profiles',
      name: 'profiles',
      component: () => ProfilesView
    }
  ]
})

export default router
