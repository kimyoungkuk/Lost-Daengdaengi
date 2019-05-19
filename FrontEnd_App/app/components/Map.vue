<template>
    <Page class="page">
        <ActionBar class="action-bar" title="map"></ActionBar>
        <GridLayout rows="*,auto">
                <Mapbox row = "0"
                    ref = "map"
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
                <Button row = "1" backgroundColor = "#ffffff" @swipe = "onSwipe" padding = "10"></Button>
        </GridLayout>     
        
    </Page>
</template>

<script>
    import * as utils from "utils/utils";
    const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
    import * as mapbox from "nativescript-mapbox";
    export default {
        data () {
            
            return { 
                makerinfo : []
            };
        },
        methods: {
            onMapReady(args) {
                this.map = args.map;
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
                    this.map.destroy();
                    this.$goto('board');
                    
                }
                console.log.unshift({
                    text: "You performed a " + direction + " swipe"
                });
            },


        }
    };
</script>

<style scoped>
    ActionBar {
        background-color: #53ba82;
        color: #ffffff;
    }

    .message {
        vertical-align: center;
        text-align: center;
        font-size: 20;
        color: #333333;
    }
</style>
