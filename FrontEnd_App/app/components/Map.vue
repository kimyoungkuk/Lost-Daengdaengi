<template>
	 <Page @loaded="loaded" ref="page">
     <ActionBar class="action-bar" title=''>
            <ActionItem @tap="$goto('makeFinderPost')">
                <button text="찾았어요" class="btn mybtn font-weight-bold" android:horizontalAlignment="left" >/>
                </button>
            </ActionItem>
            <ActionItem @tap="$goto('makeOwnerPost')" >
                <button text="찾아주세요" class="btn mybtn font-weight-bold" android:horizontalAlignment="right">/>
                </button>
            </ActionItem>
        </ActionBar>
        <GridLayout :rows="row_scale"> 
      <GridLayout rows = "*,auto,auto">
        <mapView row = "0" id="mapview" 
          :latitude="lat" 
          :longitude="lng" 
          :zoom="15" 
          :tilt="0"
          :padding="padd"
          :mapAnimationsEnabled="true"
          :myLocationButtonEnabled="true"
          @mapReady="onMapReady($event)" 
          >
          </mapView>
          <fab @tap="myLocTap" row="0" rippleColor="#ffffff" icon = "ic_menu_mylocation" class="fab-button"></fab>
      </GridLayout>
      <GridLayout row = "1" rows = "auto,*">
                <Label row = "0" backgroundColor = "#FA7268" @swipe = "onSwipe" padding = "10"></Label>
                <ScrollView row="1">
                    <WebView height="500" ref = "webview" @loadFinished="completeLoading" @loaded="webViewLoaded" id="myWebView" src="http://202.30.31.91/finderBoard"/>
                    <!-- <WebViewExt id='webview' loaded="viewLoaded" class="ann-text" :src="this.API_WEBVIEW_URL_finder"
                             textWrap="true" debugMode="true"></WebViewExt> -->
                </ScrollView>
      </GridLayout>
        </GridLayout>
    </Page>
</template>

<script>
import * as utils from "utils/utils";
import * as Gmap from "nativescript-google-maps-sdk";
import * as geolocation from "nativescript-geolocation";
import { Accuracy } from "tns-core-modules/ui/enums";
var webViewModule = require('ui/web-view');
const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
export default {
  
    data() {
      return {
        //ChangedNickName : this.$store.state.user_nickname,
        map : null,
        webView : null,
        lat :37,
        lng :127,
        padd : [40,40,40,40],
        row_scale : "*, 100",
        count : 0,
        API_WEBVIEW_URL_finder : this.$store.state.API_WEBVIEW_URL + '/finderboard'+"?key=" + this.$store.state.user_Email + "&nickname=" + this.$store.state.user_nickname,
        API_WEBVIEW_URL_finder_temp : this.$store.state.API_WEBVIEW_URL + '/finderboard'+"?key=" + this.$store.state.user_Email + "&nickname=" + this.$store.state.user_nickname,
      }
    },
  methods: {

//     viewLoaded(args){
//     let webview = args.object;
//     webview.on(WebViewExt.shouldOverrideUrlLoadingEvent, (args) => {
//         console.log(args.url);
//         console.log(args.httpMethod);
//         if (args.url != null && args.url.startsWith("https://")) {
//             console.log(args.url);
//             utilityModule.openUrl(args.url);
//             return true;
//         }else {
//             return false;
//         }
//     });
// },
         completeLoading(args){
        this.loadingComplete=false
        args.object.android.getSettings().setJavaScriptEnabled(true);
        args.object.android.getSettings().setBuiltInZoomControls(false);
      },
      loaded(args) {
    const page = args.object;
    const webview = page.getViewById('myWebView')
    

    debugger;
    //webView.url = 
    webview.on(webViewModule.WebView.loadFinishedEvent, function (args) {
        console.log(JSON.stringify(args.url));
    });
    webview.android.getSettings().setJavaScriptEnabled(true);
    webview.android.getSettings().setDisplayZoomControls(false);
    webview.android.getSettings().setBuiltInZoomControls(false);
    webview.android.getSettings().setAllowFileAccessFromFileURLs(true);
    webview.android.getSettings().setAllowUniversalAccessFromFileURLs(true);
    webview.android.getSettings().setMediaPlaybackRequiresUserGesture(false);
    webview.android.getSettings().setUseWideViewPort(true);
    webview.android.getSettings().setDomStorageEnabled(true);
  
      },



// loaded(args) {
//   var page = args.object;
//   const webview = page.getViewById('myWebView');
//   var TNSWebViewClient =
//     android.webkit.WebViewClient.extend({
//       shouldOverrideUrlLoading: function (view, url) {
//         if (url != null && url.startsWith("http://")) {
//           console.log(url);
//           // use openUrl form utils module to open the page in a browser
//           return true;
//         } else {
//           return false;
//         }
//       }
//     });
//   var TNSWebChromeClient =
//     android.webkit.WebChromeClient.extend({
//       onPermissionRequest: function (request) {
//         request.grant(request.getResources());
//       }
//     });
//     webview.android.getSettings().setJavaScriptEnabled(true);
//     webview.android.getSettings().setDisplayZoomControls(false);
//     webview.android.getSettings().setBuiltInZoomControls(false);
//     webview.android.getSettings().setAllowFileAccessFromFileURLs(true);
//     webview.android.getSettings().setAllowUniversalAccessFromFileURLs(true);
//     webview.android.getSettings().setMediaPlaybackRequiresUserGesture(false);
//     webview.android.getSettings().setUseWideViewPort(true);
//     webview.android.getSettings().setDomStorageEnabled(true);
//     webview.android.setWebViewClient(new TNSWebViewClient());
//     webview.android.setWebChromeClient(new TNSWebChromeClient());
  

// },


//   loaded(webargs) {
// const page = webargs.object

// const webview = page.getViewById('myWebView');

// webview.on(webViewModule.WebView.shouldOverrideUrlLoading, (args) => {
//     let message = "Loading initiated, please wait....";
//     if (!args.error) {
//         message = `WebView is loaded: ${args.url}`;
//     }
//     else {
//         message = `Error while loading: ${args.url} : ${args.error}`;
//     }
//     // vm.set("result", message);
//     console.log(`WebView console log messages - ${message}`);
//     if (args.url.indexOf('http://') === 0) {
      
     
//     }
// });
// webview.android.getSettings().setDisplayZoomControls(false);
//       webview.android.getSettings().setBuiltInZoomControls(false);
// },  
      onMapReady(args){
        var mView = args.object;  
        var gMap = mView.gMap;
        geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 2000,
                    timeout: 3000
        }).then(loc => {
           this.lat = loc.latitude
           this.lng = loc.longitude
        })
        gMap.myLocationEnabled=true
        console.log(gMap.myLocation)
        console.log(args.object._observers)
        console.log(mView.settings.myLocationButtonEnabled);
       // this.map.settings.setCenter({lat : 11,lng : 21})
      //  this.map.settings.setZoom(12)
      },
      myLocTap(args){
        geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 2000,
                    timeout: 3000
        }).then(loc => {
           this.lat = loc.latitude
           this.lng = loc.longitude
        })
      },
      onSwipe(args) {
                let direction =
                    args.direction == SwipeDirection.down
                        ? "down"
                        : args.direction == SwipeDirection.up
                            ? "up"
                            : args.direction == SwipeDirection.left
                                ? "left"
                                : "right";
                console.log(direction);
                if(direction == "up"){
                    this.row_scale = "70,*"
                    count = 0;
                }if(direction == "down"){
                    if(this.count == 0){
                        this.row_scale = "*,100";
                        this.count ++;
                        console.log("100")
                    }
                    else{
                        this.row_scale = "*,50";
                        this.count--;
                        console.log("50")
                    }

                }
                console.log.unshift({
                    text: "You performed a " + direction + " swipe"
                });
            },
    }
}
</script>

<style scoped>
.fab-button {
  height: 70;
  margin: 15;
  background-color: #ffffff;
  horizontal-align: right;
  vertical-align: bottom;
}
.mybtn{
  color: #FA7268;
  background-color: #FFFFFF;
}

ActionBar {
        background-color: #FA7268;
        color: #ffffff;
    }
</style>

