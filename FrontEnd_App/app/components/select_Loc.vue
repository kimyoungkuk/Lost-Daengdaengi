<template>
    <Page class="page" actionBarHidden="true">
        <GridLayout rows="*,auto">
            <GridLayout row = "0">
                <mapView row = "0" id="mapview" 
                :latitude="lat" 
                :longitude="lng" 
                :zoom="15" 
                :tilt="0"
                :mapAnimationsEnabled="true"
                :myLocationButtonEnabled="true"
                @mapReady="onMapReady($event)" 
                @coordinateTapped="mapTap($event)"
                >
                </mapView>
                <label :text="address" row ="1"/>
            </GridLayout>
                <Button class="mybtn" text = "위치 선택" row = "1" @tap = "onTap" padding = "10"></Button>
        </GridLayout>     
        
    </Page>
</template>

<script>
    import * as utils from "utils/utils";
    const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
    // import * as GmapUtils from "nativescript-google-maps-utils"
    import * as mapsModule from "nativescript-google-maps-sdk";
    import * as geolocation from "nativescript-geolocation";
    import { Accuracy } from "tns-core-modules/ui/enums";
    import makePost_ from "./makePost";
    export default {

        data () {
            return { 
                markerinfo : [],
                lat : 0,
                lng : 0,
                marker : null,
                selected_loc : {
                    lat : this.lat,
                    lng : this.lng
                },
                mapView :null,
                address : ""
            };
        },
        methods: {
            onMapReady(args) {
                var mView = args.object;
                this.marker = new mapsModule.Marker();
                this.mapView = args.object
                geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 5000,
                    timeout: 10000
                }).then(loc => {
                    this.lat = loc.latitude;
                    this.lng = loc.longitude;
                    this.marker.position = mapsModule.Position.positionFromLatLng(loc.latitude,loc.longitude);
                   
                    
                    this.$http.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+loc.latitude+","+loc.longitude+"&language=ko&key=" + 'AIzaSyBKv9vTYUpMTBV_ororyGLcbpEAmsYzwNc',{

                    }).then(res =>{
                        this.address = res.data.results[0].formatted_address
                        this.marker.title = this.address
                        this.markerinfo.push(this.marker)
                        this.mapView.addMarker(this.marker)
                        this.$store.state.selected_loc = "위치 : " + res.data.results[0].formatted_address
                    })
                    this.$store.state.ownerPost.lat = loc.latitude;
                    this.$store.state.ownerPost.lng = loc.longitude;
                    this.$store.state.FinderPost.lat = loc.latitude;
                    this.$store.state.FinderPost.lng = loc.longitude;
                })
            },
            mapTap(args){
                this.lat = args.position.latitude;
                this.lng = args.position.longitude;
                console.log(args.position.latitude)
                this.mapView.clear()
                this.marker = null;

                // this.mapView.removeMarkers();
                // this.mapView = null;
                //console.log(this.mapView.marker)
                this.marker = new mapsModule.Marker()
                this.marker.position = mapsModule.Position.positionFromLatLng(args.position.latitude,args.position.longitude);
                this.$http.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+args.position.latitude+","+args.position.longitude+"&language=ko&key=" + 'AIzaSyBKv9vTYUpMTBV_ororyGLcbpEAmsYzwNc',{

                    }).then(res =>{
                        this.address = res.data.results[0].formatted_address
                        this.marker.title = this.address
                        this.markerinfo.push(this.marker)
                        this.mapView.addMarker(this.marker)
                        // onsole.log(res.data.results[0])
                    })
               

                console.log(this.lat)
                this.$store.state.ownerPost.lat = args.position.latitude;
                this.$store.state.ownerPost.lng = args.position.longitude;
                this.$store.state.FinderPost.lat = args.position.latitude;
                this.$store.state.FinderPost.lng = args.position.longitude;
            },
            onTap(args) {
                console.log(this.$store.state.CurrentPostType);
                if(this.$store.state.CurrentPostType == true){
                    this.$goto('makePost');
                }
                else{
                    this.$goto('makePost_Finder')
                }
            },
        }
    };
</script>

<style scoped>
      .mybtn{
      color: #ffffff;
      background-color: #FA7268;
    }
    .message {
        vertical-align: center;
        text-align: center;
        font-size: 20;
        color: #333333;
    }
</style>
