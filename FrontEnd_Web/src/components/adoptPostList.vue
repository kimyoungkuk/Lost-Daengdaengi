<template>
<div class="googleFont_board">
    <div>
      <b-button-group>
        <b-button v-if="this.mob" class="btn btn-primary custom-invert" router-link to='/finderboard'>발견인 게시판</b-button>
        <b-button v-if="this.mob" class="btn btn-primary custom-invert" router-link to='/ownerboard'>유기견주 게시판</b-button>
        <b-button v-if="this.mob" class="btn btn-primary custom-invert" router-link to='/finishboard'>반환완료 게시판</b-button>
        <b-button :pressed="true" v-if="this.mob" class="btn btn-primary custom-invert" router-link to='/adopt/post/list'>분양 게시판</b-button>
      
        <b-button v-if="this.lap" class="btn btn-primary custom-invert" router-link to='/adopt/post/create'>유기견 분양글 작성</b-button>
      </b-button-group>
    </div>
    
     <div>
    <b-card-group deck deck v-for="row in formattedPosts">
        <b-card  v-for="post in row"
                :title="post.title"
                :img-src=post.imageurl
                style="max-width: 30rem; max-height: 35rem;"
                img-top>
            <p class="card-text">
                <strong>견종 : </strong>{{post.dog_type}}
            </p>
            <p class="card-text">
              <!-- <strong>찾은 날짜 : </strong>{{$moment($moment(post.lost_time).format('YYYYMMDDHH'),"YYYYMMDDHH").fromNow()}} -->
              <strong>게시날짜 : </strong>{{$moment($moment(post.posted_time).format('YYYYMMDDHH'),"YYYYMMDDHH").fromNow()}}
            </p>
            <div slot="footer">
                <!-- <b-btn variant="primary" block>상세보기</b-btn> -->
                <router-link :to="`/adopt/post/detail/${post.id}`"><b-btn class="btn btn-primary custom-btn" block>상세보기</b-btn></router-link>
            </div>
        </b-card>
    </b-card-group>
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
      key : this.$store.state.user_key,
      nickname : this.$store.state.user_nickname,
      mob : true,
      lap : false,
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
    console.log("TTT")
    let urlParams = new URLSearchParams(window.location.search);
    console.log(urlParams.get('key'))
    console.log(urlParams.get('nickname'))
    console.log("TTT")
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
          console.log("QWE111111111111111")
          console.log(this.posts)
          console.log("QWE")
          
      })
    },
  computed: {
            formattedPosts() {
          return this.posts.reduce((c, n, i) => {
              if (i % 4 === 0) c.push([]);
              c[c.length - 1].push(n);
              return c;
          }, []);
      },

      
  },
  methods:{
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

}
</script>