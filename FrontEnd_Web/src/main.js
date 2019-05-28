import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Router from 'vue-router'
import routes from './routes'
import BootstrapVue from 'bootstrap-vue'
import axios from 'axios'
import "moment/locale/ko"
import moment from 'moment'
import VueMomentJS from 'vue-momentjs'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.prototype.$http = axios
Vue.use(VueMomentJS, moment)
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
