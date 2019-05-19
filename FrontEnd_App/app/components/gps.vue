<template>
    <Page class="page">
        <button text = "post_loc" @tap = "onClick"></button>
    </Page>
</template>

<script>
    import * as geolocation from "nativescript-geolocation";
    import { Accuracy } from "tns-core-modules/ui/enums";
    import axios from "axios";
    export default {
        data() {
            return {
                watchIds: [],
                locations: []
            }
        },
        methods: {
            enableLocationTap: function() {
                geolocation.isEnabled().then(function (isEnabled) {
                    if (!isEnabled) {
                        geolocation.enableLocationRequest().then(function () { }, function (e) {
                            console.log("Error: " + (e.message || e));
                        });
                    }
                }, function (e) {
                    console.log("Error: " + (e.message || e));
                });
            },
            onClick : function(){
                geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 5000,
                    timeout: 10000
                }).then(function (loc) {
                    if (loc) {
                        //that.locations.push(loc);
                        console.log(loc.latitude);
                        console.log(loc.longitude);
                        axios.post('http://6869c462.ngrok.io/api/location_test',{
                            lat : loc.latitude,
                            lng : loc.longitude
                        }).then(res => {
                            console.log(res.data)
                        }).catch(err =>{
                            console.log(err)
                        })
                    }
                }, function (e) {
                    console.log("Error: " + (e.message || e));
                });
            },
            buttonGetLocationTap: function() {
                let that = this;
                geolocation.getCurrentLocation({
                    desiredAccuracy: Accuracy.high,
                    maximumAge: 5000,
                    timeout: 10000
                }).then(function (loc) {
                    if (loc) {
                        that.locations.push(loc);
                    }
                }, function (e) {
                    console.log("Error: " + (e.message || e));
                });
            },
            buttonStartTap: function() {
                try {
                    let that = this;
                    this.watchIds.push(geolocation.watchLocation(
                        function (loc) {
                            if (loc) {
                                that.locations.push(loc);
                            }
                        },
                        function (e) {
                            console.log("Error: " + e.message);
                        },
                        {
                            desiredAccuracy: Accuracy.high,
                            updateDistance: 1,
                            updateTime: 3000,
                            minimumUpdateTime: 100
                        }));
                } catch (ex) {
                    console.log("Error: " + ex.message);
                }
            },
            buttonStopTap: function() {
                let watchId = this.watchIds.pop();
                while (watchId != null) {
                    geolocation.clearWatch(watchId);
                    watchId = this.watchIds.pop();
                }
            },
            buttonClearTap: function() {
                this.locations.splice(0, this.locations.length);
            }
        }
    };
</script>

<style scoped lang="scss">
    // // Start custom common variables
    // @import '../app-variables';
    // // End custom common variables
    // // Custom styles
    // .fa {
    //     color: $accent-dark;
    // }
    // .info {
    //     font-size: 20;
    // }
</style>