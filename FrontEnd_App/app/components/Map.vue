<template>
	 <Page>
     <ActionBar class="action-bar" title="map">
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_back" @tap="openDrawer"/>

            <ActionItem @tap="$goto('makeFinderPost')">

                <button text="찾았어요" class="btn btn-primary" android:horizontalAlignment="right" >/>
                </button>
            </ActionItem>
            <ActionItem @tap="$goto('makeOwnerPost')" >
                <button text="찾아주세요" class="btn btn-primary" android:horizontalAlignment="right">/>
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
          <SegmentedBar @selectedIndexChange="onSelectedIndexChange">
            <SegmentedBarItem title="찾았어요"/>
            <SegmentedBarItem title="찾아주세요"/>
          </SegmentedBar>
      
      </GridLayout>
      <GridLayout row = "1" rows = "auto,*">
                <Label row = "0" backgroundColor = "#4ba5fa" @swipe = "onSwipe" padding = "10"></Label>

                <ScrollView row="1">
                    <WebView ref = "webview" loaded="onWebViewLoaded" id="myWebView" :src="this.API_WEBVIEW_URL_finder"/>
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
const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
import * as http from "http";
import { Image } from 'tns-core-modules/ui/image/image';

export default {
  
    data() {
      return {
        marker_Finder :[],
        marker_Owner :[],
        //ChangedNickName : this.$store.state.user_nickname,
        mapView : null,
        lat :37,
        lng :127,
        padd : [40,40,40,40],
        row_scale : "*, 100",
        count : 0,
        API_WEBVIEW_URL_finder : this.$store.state.API_WEBVIEW_URL + '/finderboard'+"?key=" + this.$store.state.user_Email + "&nickname=" + this.$store.state.user_nickname,
        API_WEBVIEW_URL_finder_temp : this.$store.state.API_WEBVIEW_URL + '/finderboard'+"?key=" + this.$store.state.user_Email + "&nickname=" + this.$store.state.user_nickname,
        selected :0
      }
    },
  methods: {
      onMapReady(args){
        var mView = args.object;
        this.mapView = mView;  
        var gMap = mView.gMap;
        var marker_T;
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
                          marker_T.title = res.data[i].title;
                          marker_T.userData = res.data[i];
                          this.marker_Finder.push(marker_T);
                        }
                      for(var i =0;i<this.marker_Finder.length;i++){
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
                      marker_T.title = res.data[i].title;
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
</style>