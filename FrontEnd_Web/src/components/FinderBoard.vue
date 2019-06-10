<template>
  <div class="googleFont_board">
    <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
    <!-- 발견인 게시판 & 유기견주 게시판 선택 버튼 -->
    <div>
      <b-button-group>
        <b-button :pressed="true" class="btn btn-primary custom-invert btn-size" router-link to='/finderboard'>발견인 게시판</b-button>
        <b-button class="btn btn-primary custom-invert btn-size" router-link to='/ownerboard'>유기견주 게시판</b-button>
        <b-button class="btn btn-primary custom-invert btn-size" router-link to='/finishboard'>반환완료 게시판</b-button>
        <b-button class="btn btn-primary custom-invert btn-size" router-link to='/adopt/post/list'>분양 게시판</b-button>
      </b-button-group>
    </div>
    <!-- 검색 관련 div -->
    <div>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <!-- 검색 시작시간 입력 -->
        <div><h3 style="color:#FA7268; margin-top:2%;">Lost Daengdaengi</h3></div>
        <div><h4>검색</h4></div>
        <div style="float:left; width:50%;">
          <i class="material-icons">event</i>
          <b-form-group id="input-group-1" label="검색 시작시간" label-for="input-1">
            <datepicker id="input-1" placeholder="YYYY-MM-DD" v-model="form.starttime"></datepicker>
          </b-form-group>       
        </div>
        <!-- 검색 최종시간 입력 -->
        <div style="float:left; width:50%;">
          <i class="material-icons">event</i>
          <b-form-group id="input-group-2" label="검색 최종시간" label-for="input-2">
            <datepicker id="input-2" placeholder="YYYY-MM-DD" v-model="form.finaltime"></datepicker>
          </b-form-group>
        </div>
        <!-- 검색 카테고리 -->
        <b-form-group id="input-group-4" label-for="input-4">
          <b-form-select
            id="input-4"
            v-model="form.category"
            :options="categories"
          ></b-form-select>
          <b-form-input
            id="input-3"
            v-model="form.value"
            placeholder="검색 내용을 입력하세요."
          ></b-form-input>
        </b-form-group>
        <!-- 제출 및 리셋 버튼 -->
        <b-button type="submit" class="btn btn-primary custom-btn">Search</b-button>
        <b-button type="reset" class="btn btn-primary custom-invert">Reset</b-button>
      </b-form>
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
            <strong>견종 : </strong>{{post.dog_type}}
          </p>
          <p class="card-text">
            <strong>찾은 날짜 : </strong>{{$moment($moment(post.find_time).format('YYYYMMDDHH'),"YYYYMMDDHH").fromNow()}}
          </p>
          <div slot="footer">
            <router-link :to="`/finderboard/view/${post.id}`"><b-btn class="btn btn-primary custom-btn" block>상세보기</b-btn></router-link>
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
    this.lat = urlParams.get('lat');
    this.lng = urlParams.get('lng');
    console.log(this.lat)
    console.log(this.lng)
    this.$http.get('http://202.30.31.91:8000/api/finderPosts/list')
      .then(res => {
          console.log(res.data)
          this.posts = res.data
            
          if (this.lat!=null && this.lng!=null){
            this.$http.get("http://202.30.31.91:8000/api/finderPosts/filter/with?key="+this.key+"&nickname="+this.nickname+"&lat=" + this.lat + "&lng=" + this.lng)
              .then(res => {
                this.posts = res.data
                console.log(res.data)
              })
          }
          
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

<style>
.googleFont_board {
    font-family: 'Jua', sans-serif;
    /* color: #FA7268; */
}

.btn-primary.custom-invert {
  background-color: white;
  border-color: #FA7268;
  color: #FA7268;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
}

.btn-primary.custom-invert.btn-size {
  font-size: 12px;
}

.btn-primary.custom-invert:hover:after {
  background-color: white;
  border-color: #FA7268;
  color: #FA7268;
}

/* .btn-primary.custom-invert:focus {
  background-color: white;
  border-color: #FA7268;
  color: #FA7268;
} */

#input-2 {
  width: 100%;
  flex: 1;
  text-align: center;
}

#input-1 {
  width: 100%;
  flex: 1;
  text-align: center;
}
</style>
