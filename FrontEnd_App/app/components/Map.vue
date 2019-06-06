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
          :myloction="{lat,lng}"
          @mapReady="onMapReady($event)" 
          @markerInfoWindowTapped="showDetail($event)"
          @markerSelect="markerS($event)"
          > 
          </mapView>
          <fab @tap="myLocTap" row="0" rippleColor="#ffffff" icon = "ic_menu_mylocation" class="fab-button"></fab>
          <SegmentedBar @selectedIndexChange="onSelectedIndexChange">
            <SegmentedBarItem title="찾았어요"/>
            <SegmentedBarItem title="찾아주세요"/>
          </SegmentedBar>
      
      </GridLayout>
      <GridLayout row = "1" rows = "auto,*">
                <Label row = "0" text = "X" backgroundColor = "#FA7268" @tap="onTapClose" textAlignment="right" padding = "10"></Label>
                <ScrollView row="1">
                    <WebView height="500" ref = "webview" @loadFinished="completeLoading" id="myWebView" :src="this.API_WEBVIEW_URL_finder"/>
                </ScrollView>
      </GridLayout>
        </GridLayout>
    </Page>
</template>

<script>
import * as utils from "utils/utils";
import * as mapsModule from "nativescript-google-maps-sdk";
import * as geolocation from "nativescript-geolocation";
import { Accuracy } from "tns-core-modules/ui/enums";
var webViewModule = require('ui/web-view');
const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
import * as http from "http";
import { Image } from 'tns-core-modules/ui/image/image';

function gup( name, url ) {
    if (!url) url = location.href;
    name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+name+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( url );
    return results == null ? null : results[1];
}

export default {
  
    data() {
      return {
        marker_Finder :[],
        marker_Owner :[],
        mapView : null,
        map : null,
        webView : null,
        lat :37,
        lng :127,
        padd : [40,40,40,40],
        row_scale : "*, 40",
        count : 0,
        API_WEBVIEW_URL_finder : this.$store.state.API_WEBVIEW_URL + '/finderboard'+"?key=" + this.$store.state.user_key + "&nickname=" + this.$store.state.user_nickname,
        API_WEBVIEW_URL_finder_temp : this.$store.state.API_WEBVIEW_URL + '/finderboard'+"?key=" + this.$store.state.user_key + "&nickname=" + this.$store.state.user_nickname,
        selected :0
      }
    },
  methods: {
         completeLoading(args){
        this.loadingComplete=false
        args.object.android.getSettings().setJavaScriptEnabled(true);
        args.object.android.getSettings().setBuiltInZoomControls(false);
          console.log("--------------------------")
  var query = gup('key', args.url)
  console.log(args.object)
  console.log(args.object.src)
  console.log("query" + query)

      },
      loaded(args) {
    const page = args.object;
    const webview = page.getViewById('myWebView')
 
    webview.android.getSettings().setJavaScriptEnabled(true);
    webview.android.getSettings().setDisplayZoomControls(false);
    webview.android.getSettings().setBuiltInZoomControls(false);
    webview.android.getSettings().setAllowFileAccessFromFileURLs(true);
    webview.android.getSettings().setAllowUniversalAccessFromFileURLs(true);
    webview.android.getSettings().setMediaPlaybackRequiresUserGesture(false);
    webview.android.getSettings().setUseWideViewPort(true);
    webview.android.getSettings().setDomStorageEnabled(true);
  
      },
      showDetail(args){
        if(this.selected == 1){
          this.API_WEBVIEW_URL_finder = this.$store.state.API_WEBVIEW_URL + '/finderboard/view/'+args.marker.userData.id+"?key=" + this.$store.state.key + "&nickname=" + this.$store.state.user_nickname;
          this.row_scale = "70,*"
       // console.dir(args.marker.userData.id)
        }
        else{
          this.API_WEBVIEW_URL_finder = this.$store.state.API_WEBVIEW_URL + '/ownerboard/view/'+args.marker.userData.id+"?key=" + this.$store.state.key + "&nickname=" + this.$store.state.user_nickname;
          this.row_scale = "70,*"
        }
      },
      onMapReady(args){
        var mView = args.object;
        this.mapView = mView;  
        var gMap = mView.gMap;
        var marker_T;
        console.log(this.mapView.selectedMarker)
        geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 2000,
                    timeout: 3000
        }).then(loc => {
           this.lat = loc.latitude
           this.lng = loc.longitude
        })
  
        gMap.myLocationEnabled=true
      },
      markerS(args){
        console.log(args.position)
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
      onSelectedIndexChange(args){
        var marker_T;
          if(this.mapView){
            this.mapView.clear();
            this.marker_Finder = [];
            this.marker_Owner = [];
          }
          if(this.selected == 0){
            this.$http.get(this.$store.state.API_BACKEND_URL + '/api/finderPosts/list',{
                  })
                  .then(res => {
                      for(var i =0; i<res.data.length;i++){
                          marker_T = new mapsModule.Marker();
                          marker_T.position = mapsModule.Position.positionFromLatLng(res.data[i].lat,res.data[i].lng);
                          marker_T.title = res.data[i].title +"\n(자세히 보려면 클릭)";
                          marker_T.userData = res.data[i];
                    
                          this.marker_Finder.push(marker_T);
                        }
                      for(var i =0;i<this.marker_Finder.length;i++){
                          console.log(this.marker_Finder[i].userData)
                          this.mapView.addMarker(this.marker_Finder[i]);
                        }
                      })
                  .catch(error => {console.log(error)});
            this.selected = 1;
          }
          else{
            this.$http.get(this.$store.state.API_BACKEND_URL + '/api/ownerPosts/list',{
                })
                .then(res => {
                    for(var i =0; i<res.data.length;i++){
                      marker_T = new mapsModule.Marker();
                      marker_T.position = mapsModule.Position.positionFromLatLng(res.data[i].lat,res.data[i].lng);
                      marker_T.title = res.data[i].title+"\n(자세히 보려면 클릭)";
                      marker_T.userData = res.data[i];
                      this.marker_Owner.push(marker_T);
                    }
                    for(var i =0;i<this.marker_Owner.length;i++){
                      this.mapView.addMarker(this.marker_Owner[i]);
                    }
                    })
                .catch(error => {console.log(error)});
                this.selected = 0;
          }

      },
      onTapClose(args) {
               this.row_scale = "*,40"
      }
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

