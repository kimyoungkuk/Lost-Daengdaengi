<template>
  <div>
    <div>
      <b-carousel
        :interval="3000"
        controls
        indicators
        fade
        style="text-shadow: 1px 1px 2px #333; img-width:10px;">
        <!-- Text slides with image -->
        <b-carousel-slide
          caption="대한민국 최강 유기견 플랫폼"
          text="지금 당장 시작하세요"
          :img-src= "src1"
        ></b-carousel-slide>

        <!-- Slides with custom text -->
        <b-carousel-slide
          caption="반려견을 위한 시작"
          text="여러분의 반려견을 지켜주세요"
          :img-src= "src2"
        ></b-carousel-slide>

        <b-carousel-slide
        caption="Lost DaengDaengi"
        text="자동화된 시스템을 경험하세요"
        :img-src= "src3"
  
      ></b-carousel-slide>
    </b-carousel>
    </div>
  </div>
</template>

<script>

export default {
 data() {
      return {
        slide: 0,
        sliding: null,
        counter: 45,
        max: 100,
        src1: require('../assets/1.jpg'),
        src2: require('../assets/2.jpg'),
        src3: require('../assets/3.jpg'),
      }
    },
    methods: {
    },
    created(){
console.log(this.$store.state.API_BACKEND_URL)
    }
}
</script>

<style scoped>

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
