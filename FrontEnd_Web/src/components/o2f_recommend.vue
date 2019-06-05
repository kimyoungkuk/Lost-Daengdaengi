<template>
  <div>
    <div>
      <h1>높은 유사도를 가지는 유기견들입니다.</h1>
    </div>
    <div>
      <b-card-group deck deck v-for="row in formattedPosts">
        <b-card 
          v-for="post in row"
          :title="post.title"
          :img-src="post.imageurl"
          style="max-width: 30rem;"
          img-top>
          <p class="card-text">
            <strong>ID : </strong> {{post.id}}
          </p>
          <p class="card-text">
            <strong>견종 : </strong>{{post.dog_type}}
          </p>
          <p class="card-text">
            <strong>찾은 날짜 : </strong>{{$moment($moment(post.find_time).format('YYYYMMDDHH'),"YYYYMMDDHH").fromNow()}}
          </p>
          <div slot="footer">
            <router-link :to="`/finderboard/view/${post.id}`"><b-btn variant="primary" block>상세보기</b-btn></router-link>
          </div>
        </b-card>
      </b-card-group>
    </div>
  </div>
</template>

<script>
import 'url-search-params-polyfill';
import Datepicker from 'vuejs-datepicker';
export default {
  components: {
    Datepicker
  },
  // finder 게시글 제목(title), 견종(dog_type) , 잃어버린 날짜(lost_time), imgsrc(imageurl)
  // API (/api/finderPosts/list)
  // API (/api/ownerPosts/list)
  data: function () {
    return {
      key : '',
      nickname : '',
      lat : 0,
      lng : 0,
      posts: [{title:'', dog_type:'', find_time:'', imageurl:''}],
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
    if(this.$store.state.user_Email=="" || this.$store.state.user_nickname=="")
    {
      this.$store.state.user_Email = urlParams.get('key');
      this.key = urlParams.get('key');
      this.$store.state.user_nickname = urlParams.get('nickname');
      this.nickname = urlParams.get('nickname');
      console.log(this.key)
      console.log(this.nickname)
    }
    this.lat = urlParams.get('lat');
    this.lng = urlParams.get('lng');
    console.log(this.lat)
    console.log(this.lng)
    this.$http.get(`http://202.30.31.91:8000/api/ownerPosts/recommend/${this.$route.params.query}`)
      .then(res => {
          console.log(res.data.recommend)
          this.posts = res.data.recommend
           
          
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
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      this.$http.post('http://202.30.31.91:8000/api/finderPosts/filter', {
        starttime : this.form.starttime,
        finaltime : this.form.finaltime,
        category : this.form.category,
        value : this.form.value
        // category : this.form.category,
        // value : this.form.value
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
  }
}
</script>