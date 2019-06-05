<template>
  <div id="app">
    <!-- <img alt="Formpoom logo" src="./assets/logo.png" > -->
      <!-- <b-button-group>
      <b-button router-link to='/' variant="outline-primary">Home</b-button>
      <b-button router-link to='/finderboard' variant="outline-primary">찾는 게시판</b-button>
      <b-button router-link to='/login' variant="outline-primary">로그인</b-button>
      <b-button router-link to='/aboutus' variant="outline-primary">About Us</b-button>
      <b-button variant="outline-primary">설문지 제작</b-button>
      <b-button router-link to='/answersheet' variant="outline-primary">설문하기</b-button>
    </b-button-group> -->
    <transition name="router-anim" enter-active-class="animated fadeInDown" leave-active-class="animated fadeOutDown">
      <router-view></router-view>
    </transition>
    <!-- <router-view></router-view> -->
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
    
  }
}
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

/* #app {
  background: #fff;
  width: 50%;
  padding: 30px;
  border-radius: 10px;
  margin: 50px auto 0 auto;
  height: calc(60% - 50px);
} */

.page {
  position: fixed;
  width: inherit;
}
</style>