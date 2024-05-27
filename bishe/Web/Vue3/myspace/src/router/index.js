import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HighorderData from "../views/HighorderData.vue"
import RegisterView from "../views/RegisterView.vue"
import LoginView from "../views/LoginView.vue"
import UserProfile from "../views/UserProfile.vue"
import NotfoundView from "../views/404View.vue"
import StatisticalDataView from "../views/StatisticalDataView.vue"
import SportsData from "../views/SportsData.vue"
import UserList from "../views/UserList.vue"
import SportsCharts from '../views/SportsCharts.vue'
import HistoryView from '../views/HistoryView.vue'
import MapView from '../views/MapView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/highorder/',
    name: 'highorder',
    component: HighorderData
  },
  {
    path: '/register/',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/login/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/userprofile/:userId/',
    name: 'userprofile',
    component: UserProfile
  },
  {
    path: '/404/',
    name: '404',
    component: NotfoundView
  },
  {
    path: '/statistical/',
    name: 'statistical',
    component: StatisticalDataView,
  },
  {
    path: '/sportsdata/',
    name: 'sportsdata',
    component: SportsData,
  },
  {
    path: '/userlist/',
    name: 'userlist',
    component: UserList,
  },
  {
    path: '/charts/',
    name: 'charts',
    component: SportsCharts,
  },
  {
    path: '/history/',
    name: 'history',
    component: HistoryView,
  },
  {
    path: '/map/',
    name: 'map',
    component: MapView,
  },
  {
    path: '/:catchAll(.*)',
    redirect:"/404/",
  },



  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
