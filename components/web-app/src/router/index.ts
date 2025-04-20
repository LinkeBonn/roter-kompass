import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FlyerView from "@/views/FlyerView.vue";
import PreviewView from "@/views/PreviewView.vue";
import AktionView from "@/views/AktionView.vue";
import HowToView from "@/views/HowToView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/flyer',
      name: 'flyer',
      component: FlyerView
    },
    {
      path: '/preview',
      name: 'preview',
      component: PreviewView
    },
    {
      path: '/aktion/:aktionId',
      name: 'aktion',
      component: AktionView
    },
    {
      path: '/how-to',
      name: 'how-to',
      component: HowToView
    }
  ],
})

export default router
