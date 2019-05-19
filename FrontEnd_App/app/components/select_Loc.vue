<template>
    <Page class="page" actionBarHidden="true">
        <GridLayout rows="*,auto">
            <GridLayout row = "0">
                <Mapbox 
                    accessToken="pk.eyJ1IjoicWtyODE5IiwiYSI6ImNqdjJhMjY1eTIyeDgzeW1mejl4YmZlaWsifQ.1hDcizlwRYzZqUXF6gz6tQ"
                    hideCompass="true"
                    zoomLevel="12"
                    showUserLocation="false"
                    @mapReady="onMapReady($event)">
                </Mapbox> 
            </GridLayout>
                <Button text = "선택" row = "1" backgroundColor = "#ffffff" @tap = "onTap" padding = "10"></Button>
        </GridLayout>     
        
    </Page>
</template>

<script>
    import * as utils from "utils/utils";
    const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
    import * as mapbox from "nativescript-mapbox";
    import * as geolocation from "nativescript-geolocation";
    import { Accuracy } from "tns-core-modules/ui/enums";
    import makePost_ from "./makePost";
    export default {

        data () {
            
            return { 
                makerinfo : [],
                lat : 0,
                lng : 0,
                map : null
            };
        },
        methods: {
            onMapReady(args) {
                this.map = args.map;
                const selected_loc = {
                        lat : this.lat,
                        lng : this.lng
                }
                geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 5000,
                    timeout: 10000
                }).then(loc => {
                    this.lat = loc.latitude;
                    this.lng = loc.longitude;
                    args.map.setCenter({
                        lat : this.lat,
                        lng : this.lng
                    })
                    selected_loc.update({
                        lat : this.lat,
                        lng : this.lng
                    })
                    console.log(this.lat)
                    this.$store.state.ownerPost.lat = this.lat;
                    this.$store.state.ownerPost.lng = this.lng;
                    this.$store.state.FinderPost.lat = this.lat;
                    this.$store.state.FinderPost.lng = this.lng;
                })
                args.map.addMarkers([
                    selected_loc,
                ])
                console.log(selected_loc)

                args.map.setOnMapClickListener((point) => {
                    this.lat = point['lat'];
                    this.lng = point['lng'];
                    selected_loc.update({
                        lat : this.lat,
                        lng : this.lng
                    })
                    this.$store.state.FinderPost.lat = this.lat;
                    this.$store.state.FinderPost.lng = this.lng;
                    this.$store.state.ownerPost.lat = this.lat;
                    this.$store.state.ownerPost.lng = this.lng;
                });
                // console.log(this.makerinfo)
            },
            onTap(args) {
                //makePost_.lat = this.lat;
                //makePost_.lng = this.lng;
                this.map.destroy();
                console.log(this.$store.state.CurrentPostType);
                if(this.$store.state.CurrentPostType == true){
                    this.$goto('makePost');
                }
                else{
                    this.$goto('makePost_Finder');
                }
            },


        }
    };
</script>

<style scoped>
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
