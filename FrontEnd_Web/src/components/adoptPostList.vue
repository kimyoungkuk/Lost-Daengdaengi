<template>
<div>
    <div>
      <b-button-group>
        <b-button v-if="this.mob" router-link to='/finderboard' variant="outline-primary">발견인 게시판</b-button>
        <b-button v-if="this.mob" router-link to='/ownerboard' variant="outline-primary">유기견주 게시판</b-button>
        <b-button v-if="this.mob" router-link to='/finishboard' variant="outline-primary">반환완료 게시판</b-button>
        <b-button v-if="this.mob" router-link to='/adopt/post/list' variant="outline-primary">분양 게시판</b-button>
      
        <b-button v-if="this.lap" router-link to='/adopt/post/create' variant="outline-primary">유기견 분양글 작성</b-button>
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
                <strong>ID : </strong> {{post.id}}
            </p>
            <p class="card-text">
                <strong>견종 : </strong>{{post.dog_type}}
            </p>
            <p class="card-text">
              <!-- <strong>찾은 날짜 : </strong>{{$moment($moment(post.lost_time).format('YYYYMMDDHH'),"YYYYMMDDHH").fromNow()}} -->
              <strong>게시날짜 : </strong>{{post.posted_time}}
            </p>
            <div slot="footer">
                <!-- <b-btn variant="primary" block>상세보기</b-btn> -->
                <router-link :to="`/adopt/post/detail/${post.id}`"><b-btn variant="primary" block>상세보기</b-btn></router-link>
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
      posts: [{title:'', dog_type:'', imageurl:''}],
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
          console.log("QWE")
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