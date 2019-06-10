<template>
<div class="googleFont_board">
  <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
    <div>
      <b-button-group>
        <b-button v-if="this.mob" class="btn btn-primary custom-invert btn-size" router-link to='/finderboard'>발견인 게시판</b-button>
        <b-button v-if="this.mob" class="btn btn-primary custom-invert btn-size" router-link to='/ownerboard'>유기견주 게시판</b-button>
        <b-button v-if="this.mob" class="btn btn-primary custom-invert btn-size" router-link to='/finishboard'>반환완료 게시판</b-button>
        <b-button :pressed="true" v-if="this.mob" class="btn btn-primary custom-invert btn-size" router-link to='/adopt/post/list'>분양 게시판</b-button>
      
        <b-button v-if="this.lap" class="btn btn-primary custom-invert" router-link to='/adopt/post/create'>유기견 분양글 작성</b-button>
      </b-button-group>
    </div>

    <div>
      <b-list-group deck>
        <b-list-group-item
        class="listBoardStyle"
        v-for="post in filteredPosts">
          <div class="listContentLeft">
            <img class="listImage" v-bind:src="post.imageurl" alt="alt 텍스트">
            <!-- {{post.imageurl}} -->
          </div>
          <div class="listContentRight">
            <h3><b-badge variant="info">분양</b-badge>&nbsp{{post.title}}</h3>
            <h5><li>견종 : {{post.dog_type}}</li></h5>
            <h5><li>게시 날짜 : {{$moment($moment(post.posted_time).format('YYYYMMDDHH'),"YYYYMMDDHH").fromNow()}}</li></h5>
            <router-link :to="`/adopt/post/detail/${post.id}`">
              <b-button class="btn btn-primary custom-list">상세보기</b-button>
            </router-link>
          </div>
        </b-list-group-item>
      </b-list-group>
    </div>
     <div class="text-xs-center">
    <v-pagination
      v-model="page"
      :length="this.len"
      :total-visible="5"
    ></v-pagination>
  </div>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker';
export default {
  components: {
    Datepicker
  },
  // finder 게시글 제목(title), 견종(dog_type) , 잃어버린 날짜(lost_time), imgsrc(imageurl)
  data: function () {
    return {
      page: 1,
      key : this.$store.state.user_key,
      nickname : this.$store.state.user_nickname,
      mob : true,
      lap : false,
      len : 0,
      posts: [{title:'', dog_type:'', imageurl:'', posted_time:''}],
      form: {
          starttime: null,
          finaltime: null,
          category: null,
          value: '',
      },
      categories: [{ text: '선택하세요.', value: null }, '견종', '작성자', '내용'],
      show: true
    }
  },
  created(){
    let urlParams = new URLSearchParams(window.location.search);
    if(this.$store.state.user_nickname=="Guest"){
      this.$store.state.user_key = urlParams.get('key');
      this.$store.state.user_nickname = urlParams.get('nickname');
    }
    this.key = this.$store.state.user_key
    if(this.key=='adopt_admin'){
        console.log("ZCX")
        console.log(this.key)
        this.mob=false
        this.lap=true
    }
    this.$http.get('http://202.30.31.91:8000/adopt/post/list')
      .then(res => {
          this.posts = res.data
                 this.fetchData()
          this.len = this.posts.length / 5 
          if(this.posts.length % 5 >= 1){
            this.len += 1
          }
          this.len = Math.floor(this.len)
      })
    },
  methods:{
        fetchData () {
      this.filteredPosts = this.posts.slice((this.page - 1) * 5, (this.page) * 5)
    },
      createPost(){
          if(this.key=='adopt_admin'){

            this.$router.push("/adopt/post/create");
          }
          else{
              alert("권한이 없습니다.")
              this.$router.push("/adopt/login");
          }

      }
    

  },
    watch: {
    page: function () {
      this.fetchData()
    },
  }

}
</script>