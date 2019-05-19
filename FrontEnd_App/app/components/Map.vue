<template>
    <Page class="page">
        <ActionBar class="action-bar" title="Map"></ActionBar>
        <GridLayout :rows="row_scale">
            <GridLayout row = "0">
                <Mapbox
                    accessToken="pk.eyJ1IjoicWtyODE5IiwiYSI6ImNqdjJhMjY1eTIyeDgzeW1mejl4YmZlaWsifQ.1hDcizlwRYzZqUXF6gz6tQ"
                    mapStyle="traffic_day"
                    latitude="37.532600"
                    longitude="127.024612"
                    hideCompass="true"
                    zoomLevel="12"
                    showUserLocation="false"
                    disableZoom="false"
                    disableRotation="false"
                    disableScroll="false"
                    disableTilt="false"
                    defaultLanguage = "ko"
                    @mapReady="onMapReady($event)">
                </Mapbox>
                <fab @tap = "onTap" row="0" rippleColor="#ffffff" class="fab-button"></fab>
            </GridLayout>
            <GridLayout row = "1" rows = "auto,*">
                <Label row = "0" backgroundColor = "#4ba5fa" @swipe = "onSwipe" padding = "10"></Label>
                <ScrollView row="1">
                    <WebView loaded="onWebViewLoaded" id="myWebView" src="http://192.168.43.210:8080/finderboard" />
                </ScrollView>
            </GridLayout>
        </GridLayout>     

    </Page>
</template>

<script>
    import * as utils from "utils/utils";
    const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
    import * as mapbox from "nativescript-mapbox";
    import * as geolocation from "nativescript-geolocation";
    import { Accuracy } from "tns-core-modules/ui/enums";

    export default {
        data () {
            
            return { 
                makerinfo : [],
                map : null,
                row_scale : "100,auto",
                count : 0
            };
        },
        methods: {
            onTap(args){
                console.log("Tap");
                geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 5000,
                    timeout: 10000
                }).then(loc => {
                    console.log(loc)
                    this.map.setCenter({
                        lat : loc.latitude,
                        lng : loc.longitude
                    })
                })
            },
            onMapReady(args) {
                
                this.map = args.map;
                console.log(this.map)
                args.map.getUserLocation().then(data =>{
                    console.log(data.speed);
                    console.log("123123");
                })
                 args.map.setOnMapClickListener((point) => console.log(`Map tapped: ${JSON.stringify(point)}`));
                //map.setLayoutProperty('country-label', 'text-field', ['get', 'name_ko']);
                this.$http.get(this.$store.state.API_URL + '/api/ownerPosts/list',{
                })
                .then(res => {
                    args.map.addMarkers(res.data)
                    console.log(res.data);
                    })
                .catch(error => {console.log(error)});
                // console.log(this.makerinfo)
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
    };
</script>

<style scoped>
.fab-button {
  height: 70;
  margin: 15;
  background-color: #ff4081;
  horizontal-align: right;
  vertical-align: bottom;
}
    ActionBar {
        background-color: #4ba5fa;
        color: #ffffff;
    }

    .message {
        vertical-align: center;
        text-align: center;
        font-size: 20;
        color: #333333;
    }
</style>
