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
    <router-view></router-view>

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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>