<template>
	 <Page >
     <GridLayout>
    <mapView latitude="37.532600" longitude="127.024612" mapAnimationsEnabled="true"
    								zoom="9"  
    								tilt="12"
                    @mapReady="onMapReady" />
      </GridLayout>
    </Page>
</template>

<script>
import * as utils from "utils/utils";
import * as Gmap from "nativescript-google-maps-sdk";
export default {
  
    data() {
      return {
        //ChangedNickName : this.$store.state.user_nickname,
        map : null,
      }
    },
  methods: {
      onMapReady(args){
        this.map = args.object;  
        console.log(this.map)
       // this.map.setCenter({lat : 37,lng : 127})
      }
    }
}
</script>

<style scoped>

</style>