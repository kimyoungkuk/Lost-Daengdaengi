<template>
<div class="googleFont_board">
  <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
  <div>
    <b-button-group>
        <b-button class="btn btn-primary custom-invert btn-size" router-link to='/finderboard'>발견인 게시판</b-button>
        <b-button class="btn btn-primary custom-invert btn-size" router-link to='/ownerboard'>유기견주 게시판</b-button>
        <b-button :pressed="true" class="btn btn-primary custom-invert btn-size" router-link to='/finishboard'>반환완료 게시판</b-button>
        <b-button class="btn btn-primary custom-invert btn-size" router-link to='/adopt/post/list'>분양 게시판</b-button>
    </b-button-group>
    </div>
     <div>
    <b-card-group deck>
        <b-card v-for="post in filteredPosts"
                :title="post.title"
                :img-src="post.imageurl"
                style="max-width: 30rem;"
                img-top>
            <p class="card-text">
                <strong>견종 : </strong>{{post.dog_type}}
            </p>
            <p class="card-text">
              <!-- <strong>찾은 날짜 : </strong>{{$moment($moment(post.lost_time).format('YYYYMMDDHH'),"YYYYMMDDHH").fromNow()}} -->
              <strong>반환완료</strong>
            </p>
        </b-card>
    </b-card-group>
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
      page : 1,
      filteredPosts: [],
      key : this.$store.state.user_key,
      nickname : this.$store.state.user_nickname,
      lat : 0,
      lng : 0,
      len : 0,
      posts: [{title:'', dog_type:'', lost_time:'', imageurl:''}],
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
    this.lat = urlParams.get('lat');
    this.lng = urlParams.get('lng');
    this.$http.get('http://202.30.31.91:8000/api/finishPosts/list')
      .then(res => {
        this.posts = res.data;
        this.fetchData()
           this.len = this.posts.length / 5 
          if(this.posts.length % 5 >= 1){
            this.len += 1
          }
          this.len = Math.floor(this.len)
          console.log(res.data)
      })
    },
  methods:{
      fetchData () {
      this.filteredPosts = this.posts.slice((this.page - 1) * 5, (this.page) * 5)
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$http.post('http://202.30.31.91:8000/api/ownerPosts/filter', {
        starttime : this.form.starttime,
        finaltime : this.form.finaltime,
        category : this.form.category,
        value : this.form.value
      }).then(res => {
          console.log(res.data)
          this.posts = res.data
      })
      alert(JSON.stringify(this.form))
      console.log(this.form)
    },
    onReset(evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.starttime = null
      this.form.finaltime = null
      this.form.category = null
      this.form.value = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
  },
  watch: {
    page: function () {
      this.fetchData()
    },
  }
}
</script>
