import Vue from 'nativescript-vue'
import Main from './components/Main'
import VueDevtools from 'nativescript-vue-devtools'
import router from './router'

Vue.prototype.$router = router

Vue.prototype.$goto = function (to, options) {
  this.$navigateTo(this.$router[to], options)
}

if(TNS_ENV !== 'production') {
  Vue.use(VueDevtools)
}
// Prints Vue logs when --env.production is *NOT* set while building
Vue.config.silent = (TNS_ENV === 'production')


new Vue({
  render: h => h('frame', [h(Main)])
}).$start()
