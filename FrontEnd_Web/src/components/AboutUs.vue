<template>
  <div>
    <div>
      <b-carousel
        :interval="3000"
        controls
        indicators
        fade
        style="text-shadow: 2px 2px 4px #333; img-width:15px;">
        <b-carousel-slide
          caption="현장을 확인합니다"
          text="실종현장 확인. 그리고 그 부근을 신속히 이동하면서 탐문합니다"
          :img-src= "src1"
        ></b-carousel-slide>

        <b-carousel-slide
          caption="전단지배포"
          text="실종지역에 전단지를 집중 배포. LDApp에서 제공하는 전단지를 활용하세요"
          :img-src= "src2"
        ></b-carousel-slide>

        <b-carousel-slide
          caption="방문확인"
          text="실종장소 주변의 관공서, 경찰서, 보호소 등을 방문해 확인 후 전단지를 전달하세요"
          :img-src= "src3"
        ></b-carousel-slide>
         <b-carousel-slide
          caption="App과 인터넷활용"
          text="App과 인터넷을 통해 실종신고를 하고 실시간으로 제보를 확인하세요."
          :img-src= "src4"
        ></b-carousel-slide>
         <b-carousel-slide
          caption="원점에서 재점검"
          text="같은 지역을 계속 반복하지말고 원점에서 다시 점검. 점차 점검지역을 확대하세요"
          :img-src= "src5"
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
        src1: require('../assets/a1.jpg'),
        src2: require('../assets/a2.jpg'),
        src3: require('../assets/a3.jpg'),
        src4: require('../assets/a4.jpg'),
        src5: require('../assets/a5.jpg')
      }
    },
    methods: {

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
