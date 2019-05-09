import Vue from 'nativescript-vue'
import Main from './components/Main'
import VueDevtools from 'nativescript-vue-devtools'
import router from './router'
import store from './store'
import { TNSFontIcon, fonticon } from './nativescript-fonticon';

Vue.prototype.$router = router
Vue.prototype.$goto = function (to, options) {
  this.$navigateTo(this.$router[to], options)
}


TNSFontIcon.debug = false;
TNSFontIcon.paths = {
    'fa': './fonts/font-awesome.css',
    'ion': './fonts/ionicons.css',
};
TNSFontIcon.loadCss();


Vue.filter('fonticon', fonticon);
Vue.registerElement("Mapbox", () => require("nativescript-mapbox").MapboxView)

if(TNS_ENV !== 'production') {
  Vue.use(VueDevtools)
}
// Prints Vue logs when --env.production is *NOT* set while building
Vue.config.silent = (TNS_ENV === 'production')


new Vue({
  store,
  render: h => h('frame', [h(Main)])
}).$start()
