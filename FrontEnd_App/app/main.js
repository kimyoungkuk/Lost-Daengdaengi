import Vue from 'nativescript-vue'
import Main from './components/Main'
import VueDevtools from 'nativescript-vue-devtools'
import router from './router'
// import axios from 'axios'
// import VueAxios from 'vue-axios'
import store from './store'
import RadDataForm from 'nativescript-ui-dataform/vue'
import { TNSFontIcon, fonticon } from './nativescript-fonticon';

Vue.prototype.$router = router
Vue.prototype.$goto = function (to, options) {
  this.$navigateTo(this.$router[to], options)
}

Vue.use(RadDataForm);
// Vue.use(VueAxios, axios)

// Vue.config.productionTip = false

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

var firebase = require("nativescript-plugin-firebase");
firebase
  .init({
    // Optionally pass in properties for database, authentication and cloud messaging,
    // see their respective docs.
  })
  .then(
    function(instance) {
      console.log("firebase.init done");
    },
    function(error) {
      console.log("firebase.init error: " + error);
    }
  );

new Vue({
  store,
  render: h => h('frame', [h(Main)])
}).$start()
