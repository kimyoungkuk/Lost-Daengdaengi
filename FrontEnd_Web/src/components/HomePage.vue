<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      fade
      background="#ababab"
      img-width="80%"
      img-height="200"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        caption="대한민국 최강 유기견 플랫폼"
        text="지금 당장 시작하세요"
        img-src="https://cdn.pixabay.com/photo/2016/01/05/17/51/dog-1123016_960_720.jpg"
        background
      ></b-carousel-slide>

      <!-- Slides with custom text -->
            <b-carousel-slide
        caption="Lost DaengDaengi"
        text="여러분의 반려견을 지켜주세요"
        img-src="https://cdn.pixabay.com/photo/2016/01/19/17/41/friends-1149841_960_720.jpg"
        background
      ></b-carousel-slide>

                  <b-carousel-slide
        caption="Lost DaengDaengi"
        text="자동화된 시스템을 경험하세요"
        img-src="https://cdn.pixabay.com/photo/2016/11/29/05/09/child-1867463_960_720.jpg"
        background
      ></b-carousel-slide>

      <!-- <b-carousel-slide img-src="https://cdn.pixabay.com/photo/2016/01/19/17/41/friends-1149841_960_720.jpg">
        <h1>여러분의 반려견을 지켜주세요</h1>
      </b-carousel-slide> -->

      <!-- Slides with image only -->
      <!-- <b-carousel-slide img-src="https://cdn.pixabay.com/photo/2016/11/29/05/09/child-1867463_960_720.jpg">
        <h1>자동화된 찾기 시스템을 경험하세요</h1>
      </b-carousel-slide> -->

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <!-- <b-carousel-slide>
        <img
          slot="img"
          class="d-block img-fluid w-100"
          width="1024"
          height="480"
          src="https://picsum.photos/1024/480/?image=55"
          alt="image slot"
        >
      </b-carousel-slide> -->

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
      <!-- <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
          a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
        </p>
      </b-carousel-slide> -->
    </b-carousel>

    <!-- <p class="mt-4">
      Slide #: {{ slide }}<br>
      Sliding: {{ sliding }}
    </p> -->
      <b-footer
    dark
    height="auto"
  >
    <b-card
      class="flex"
      title="2019 Capstone Design"
    >
    <b-card-text>
        <strong>Team Bohemian Capsody <br/> AJOU Univ.<br/></strong>&copy; 2019 김영국 | 박신혁 | 박찬영 | 최순원 
      </b-card-text>
    </b-card>
  </b-footer>
  </div>
  
</template>

<script>
export default {
 data() {
      return {
        slide: 0,
        sliding: null,
        counter: 45,
        max: 100
      }
    },
    methods: {
      clicked() {
        this.counter = Math.random() * this.max
        console.log('Change progress to ' + Math.round(this.counter * 100) / 100)
      },
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3 {
  margin: 40px 0 0;
}
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
