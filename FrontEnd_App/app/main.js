import Vue from 'nativescript-vue'
// import Main from './components/Main'
import VueDevtools from 'nativescript-vue-devtools'
import router from './router'
import store from './store'
import axios from 'axios'
import RadDataForm from 'nativescript-ui-dataform/vue'
import { TNSFontIcon, fonticon } from './nativescript-fonticon';
import ButtonPlugin from 'nativescript-material-button/vue';
import CardViewPlugin from 'nativescript-material-cardview/vue';
import FabPlugin from "nativescript-vue-fab"
import store_ from '~/store'
import sideDrawer from '~/components/sideDrawer'
import drawerContent from '~/components/drawerContent'

Vue.use(ButtonPlugin);
Vue.use(CardViewPlugin);
Vue.use(FabPlugin)

Vue.prototype.$router = router
Vue.prototype.$goto = function (to, options) {
  this.$navigateTo(this.$router[to], options)
}


// Vue.use(VueAxios, axios)

// Vue.config.productionTip = false

Vue.prototype.$http = axios
Vue.use(axios);

Vue.registerElement(
  'Fab',
  () => require('nativescript-floatingactionbutton').Fab
);
Vue.registerElement('RadSideDrawer', () => require('nativescript-ui-sidedrawer').RadSideDrawer);
Vue.config.productionTip = false

Vue.use(RadDataForm);

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
    store_,
    render (h) {
      return h(
        sideDrawer,
        [
          h(drawerContent, { slot: 'drawerContent' }),
          h(router.main, { slot: 'mainContent' })
        ]
      )
    }
  }).$start()