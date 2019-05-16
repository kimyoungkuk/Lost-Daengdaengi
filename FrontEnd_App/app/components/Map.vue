<template>
    <Page class="page">
        <ActionBar class="action-bar" title="map"></ActionBar>
        <GridLayout>
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
                    @mapReady="onMapReady($event)">
                </Mapbox>
        </GridLayout>
    </Page>
</template>

<script>
    import * as utils from "utils/utils";
    import axios from 'axios';
    export default {
        data () {
            
            return { 
                makerinfo : []
            };
        },
        methods: {
            onMapReady(args) {
                axios.get("http://210.107.198.174:8000/LDapp/dog_shelter_list",{
                })
                .then(res => {console.log(res.data)})
                .catch(error => {console.log(error)});
                
                //console.log(this.makerinfo)
            }
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
