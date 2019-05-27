import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import routes from './routes'
import BootstrapVue from 'bootstrap-vue'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.prototype.$http = axios

Vue.use(BootstrapVue)
Vue.use(Router)
Vue.config.productionTip = false


const router = new Router({
  pageRouting: true,
  mode: 'history',
  scrollBehavior: () => ({y: 0}),
  routes
})

new Vue({
  router,
  render: h => h(App),
  
}).$mount('#app')
