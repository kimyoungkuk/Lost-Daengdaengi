<template>
  <div>
    <!-- 발견인 게시판 & 유기견주 게시판 선택 버튼 -->
    <div>
      <b-button-group>
        <b-button router-link to='/finderboard' variant="outline-primary">발견인 게시판</b-button>
        <b-button router-link to='/ownerboard' variant="outline-primary">유기견주 게시판</b-button>
      </b-button-group>
    </div>
    <!-- 검색 관련 div -->
    <div>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <!-- 검색 내용 입력 -->
        <b-form-group id="input-group-2" label="검색 내용" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.input"
            required
            placeholder="검색 내용을 입력하세요."
          ></b-form-input>
        </b-form-group>
        <!-- 검색 카테고리 -->
        <b-form-group id="input-group-3" label="검색 카테고리" label-for="input-3">
          <b-form-select
            id="input-3"
            v-model="form.category"
            :options="categories"
            required
          ></b-form-select>
        </b-form-group>
        <!-- 제출 및 리셋 버튼 -->
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
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
export default {
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
          input: '',
          category: null,
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
        this.$http.post('http://202.30.31.91:8000/api/finderPosts/filter/dogType', {
            dog_type: this.form.input 
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
        this.form.input = ''
        this.form.category = null
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
}
}
</script>