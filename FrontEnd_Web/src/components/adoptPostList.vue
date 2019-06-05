<template>
<div>
    <div>
      <b-button-group>
      <b-button router-link to='/adopt/post/create' variant="outline-primary">글쓰기</b-button>
      </b-button-group>
    </div>
    <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <!-- 검색 시작시간 입력 -->
        <b-form-group id="input-group-1" label="검색 시작시간" label-for="input-1">
          <datepicker id="input-1" placeholder="검색을 시작할 기간을 입력하세요" v-model="form.starttime"></datepicker>
        </b-form-group>
        <!-- 검색 최종시간 입력 -->
        <b-form-group id="input-group-2" label="검색 최종시간" label-for="input-2">
          <datepicker id="input-2" placeholder="검색을 끝낼 기간을 입력하세요" v-model="form.finaltime"></datepicker>
        </b-form-group>
        <!-- 검색 내용 입력 -->
     <b-form-group id="input-group-3" label="검색 내용" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="form.value"
          placeholder="검색 내용을 입력하세요."
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-4" label="검색 카테고리" label-for="input-4">
        <b-form-select
          id="input-4"
          v-model="form.category"
          :options="categories"
        ></b-form-select>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
     </div>
     <div>
    <b-card-group deck deck v-for="row in formattedPosts">
        <b-card  v-for="post in row"
                :title="post.title"
                :img-src=post.imageurl
                style="max-width: 30rem;"
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
                <router-link :to="`/ownerboard/view/${post.id}`"><b-btn variant="primary" block>상세보기</b-btn></router-link>
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
      key : this.$store.state.user_Email,
      nickname : this.$store.state.user_nickname,
      lat : 0,
      lng : 0,
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
    this.$http.get('http://202.30.31.91:8000/adopt/post/list')
      .then(res => {
          console.log(res.data)
          this.posts = res.data

          
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
    

  },

}
</script>