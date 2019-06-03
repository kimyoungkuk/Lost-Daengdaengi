<template>
    <v-flex class="in_board-view">
      <b-card-group deck>
        <b-card header-tag="header" footer-tag="footer">
          <!-- <h6 slot="header" class="mb-0">
            <b-badge variant="dark">작성자</b-badge>
            {{this.form.writer}}
            <b-badge variant="dark">찾은 날짜</b-badge>
            {{this.form.find_time}}
            <b-badge variant="dark">조회수</b-badge>
            {{this.form.view_count}}
            <br>
            <b-badge variant="dark">제목</b-badge>
            {{this.form.title}}
            <b-badge variant="dark">견종</b-badge>
            {{this.form.dog_type}}
          </h6> -->
          <div class="div_header" slot="header">
            <b>Lost-Daengdaengi</b><b style="float:right;">조회:{{this.form.view_count}}</b>
          </div>

          <div>
            <v-layout>
              <v-flex xs12 sm6 offset-sm3>
                <v-card>
                  <!-- 이미지 불러오기 -->
                  <v-img class="white--text" height="300px" :src="this.form.imageurl">
                    <v-container fill-height fluid>
                      <v-layout fill-height>
                        <v-flex xs12 align-end flexbox>
                          <span class="headline">{{this.form.dog_type}}</span>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-img>
                  <!-- 유기견 정보 출력 -->
                  <v-card-title>
                    <div>
                      <p>
                        <b-button id="button1" variant="danger"><b>발견</b></b-button>
                        <span>&nbsp&nbsp&nbsp<b>{{this.form.title}}</b></span><br>
                      </p>
                      <span><b>&middot</b>&nbsp날&nbsp&nbsp&nbsp&nbsp짜 : {{this.form.find_time}}</span><br>
                      <span><b>&middot</b>&nbsp연락처 : {{this.form.phone_num}}</span><br>
                      <span><b>&middot</b>&nbsp아이디 : {{this.user_nickname}}</span><br>
                      <span><b>&middot</b>&nbsp보호소 : {{this.form.shelter_name}}</span><br>
                      <span><b>&middot</b>&nbsp특&nbsp&nbsp&nbsp&nbsp징 : {{this.form.dog_feature}}</span>
                    </div>
                  </v-card-title>
                  <!-- SHARE, EXPLORE, REPORT 버튼 -->
                  <v-card-actions>
                    <v-btn flat color="orange">Share</v-btn>
                    <v-btn flat color="orange">Explore</v-btn>
                    <v-btn flat color="orange" v-b-modal.modal-prevent-closing v-on:click="reportBoard">report</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </div>

          <h6 slot="footer" v-for="item in comments" v-bind:key="item.id">
            <p class="comment_name">{{item.user_nickname}}</p>&emsp;
            <p class="comment_date">{{item.commented_date}}</p>
            <div class="comment">
              <p class="comment">{{item.contents}}</p>
              <b-badge
                v-if="userId===item.id || admin === 1"
                pill
                href="#"
                v-on:click="deleteComment(item._id)"
                variant="danger"
                size="sm"
              >삭제</b-badge>
            </div>
            <hr class="horizontal">
          </h6>
          <p class="card-text">{{this.form.contents}}</p>
        </b-card>
      </b-card-group>
      <v-flex>
        <h4>
          <b-badge variant="dark">댓글</b-badge>
        </h4>
        <b-form @submit.prevent="addComment" v-on:keyup.enter="addComment">
          <b-form-textarea
            class="comment_input"
            placeholder="댓글을 입력하세요."
            rows="2"
            max-rows="6"
            v-model="contents"
          ></b-form-textarea>
          <v-flex> 
            <b-button class="comment" type="submit" variant="primary" size="sm">댓글 작성(Enter)</b-button>
          </v-flex>
        </b-form>
      </v-flex>
      <v-flex>
      <b-button-group size="sm">
        <b-button v-on:click="toBoard" class="view_button" variant="primary">목록</b-button>
        <b-button
          v-if="userId == form.userId || admin === 1"
          v-on:click="updateBoard"
          variant="primary"
        >수정</b-button>
        <b-button
          v-if="userId == form.userId || admin === 1"
          v-on:click="deleteBoard"
          variant="danger"
        >삭제</b-button>
        <!-- <b-button v-b-modal.modal-prevent-closing>신고</b-button> -->
      </b-button-group>
      </v-flex>

    <!-- <div class="mt-3">
      Submitted Names:
      <div v-if="submittedNames.length === 0">--</div>
      <ul v-else class="mb-0 pl-3">
        <li v-for="name in submittedNames">{{ name }}</li>
      </ul>
    </div> -->

      <b-modal
        id="modal-prevent-closing"
        ref="modal"
        title="게시글이 이상한가요?"
        @show="resetModal"
        @hidden="resetModal"
        @ok="handleOk"
      >
        <form ref="form" @submit.stop.prevent="handleSubmit">
          <b-form-group
            :state="nameState"
            label="신고내용을 입력해주세요"
            label-for="name-input"
            invalid-feedback="신고내용이 입력되지 않았습니다."
          >
          <b-form-input
            id="name-input"
            v-model="report_contents"
            :state="nameState"
            required
          ></b-form-input>
          </b-form-group>
        </form>
      </b-modal>


    </v-flex>
  
</template>

<script>
import axios from "axios";
export default {
  name: "boardView",
  data() {
    return {
        name: '',
        nameState: null,
        submittedNames: [],

      form: {
        _id: this.$route.params.id,
        id: "",
        title: "",
        imageurl: "",
        find_time: "",
        view_count: "",
        dog_type: "",
        dog_feature: "",
        phone_num: "",
        shelter_name: "",
      },
      comments: [
          {
            user_key: "",
            user_nickname: "",
            contents: "",
            commented_date: new Date(),
            commented_post_type: '',
            commented_post: Number,
          }
        ],
      contents: "",
      user_nickname: "",
      commented_post_type: "",
      commented_post :Number,
      admin: "",
      date: new Date()
    };
  },
  created() {
    this.getBoardDetail();
    this.getUserId();
  },
  methods: {
    getUserId() {
      this.$http.get("/api/profile/user").then(res => {
        this.userId = res.data.username;
        this.admin = res.data.isAdmin;
      });
    },
    getBoardDetail() {
      this.$http
        .get(
          `http://202.30.31.91:8000/api/finderPosts/detail/${
            this.$route.params.id
          }`
        )
        .then(res => {
          console.log(res.data.post[0]);
          console.log(res.data.comments)
          this.form = res.data.post[0];
          this.comments = res.data.comments
          console.log(this.form);
          this.form.find_time = this.$moment(this.form.find_time).format(
            "LLLL"
          );
          for (var i = 0; i < this.form.comments.length; i++) {
            this.form.comments[i].createAt = this.$moment(
              this.form.comments[i].createAt
            ).format("LLLL");
          }
        });
    },
    deleteBoard() {
      this.$http
        .delete(`/api/board/posts/${this.$route.params.id}`)
        .then(res => {
          const status = res.status;
          if (status === 200) {
            alert("정상적으로 삭제되었습니다.");
            this.$router.push("/board");
          } else if (status === 203) {
            alert("해당 권한이 존재하지 않습니다.");
            this.$router.push("/board");
          }
        })
        .catch(err => {
          alert(err);
        });
    },
    toBoard() {
      this.$router.push("/finderboard");
    },
    updateBoard() {
      this.$http.get(`/api/board/posts/${this.$route.params.id}`).then(res => {
        const status = res.status;
        if (status === 200) {
          this.$router.push({
            path: "/update/:id",
            name: "board-update",
            params: {
              id: this.$route.params.id
            }
          });
        } else if (status === 203) {
          alert("해당 권한이 존재하지 않습니다.");
          this.$router.push("/board");
        }
      });
    },
    reportBoard() {
      console.log("ASDASD");
    },
    addComment() {
      let comment = {
        user_key: "",
        user_nickname: "",
        contents: "",
        commented_post: Number,
        commented_post_type: ""
      };
      comment.user_key = "pgd0919@gmail.com"
      comment.user_nickname = "ChanYoung"
      comment.contents = this.contents;
      comment.commented_post = this.form.id;
      comment.commented_post_type = "finder"
      // this.$http.post(`http://202.30.31.91:8000/api/comments/create`, {
      axios.post(`http://202.30.31.91:8000/api/comments/create`, {
      user_key : "pgd0919@gmail.com",
      user_nickname : "ChanYoung",
      contents : comment.contents,
      commented_post : comment.commented_post,
      commented_post_type : "finder"
      })
      .then(res => {
        console.log(res.data);
        console.log("QWEQWE");
      });
      this.contents = "";
  
      this.getBoardDetail();
    },
    deleteComment(_id) {
      this.$http
        .delete(`/api/board/comment`, {
          data: { boardId: this.$route.params.id, commentId: _id }
        })
        .then(res => {
          const status = res.status;
          if (status === 200) {
            alert("댓글이 삭제되었습니다.");
            this.getBoardDetail();
          } else if (status === 203) {
            alert("해당 권한이 존재하지 않습니다.");
            this.$router.push("/board");
          }
        });
    },
    createReport() {
      let report = {
        user_nickname: "",
        report_contents: "",
        reported_post: Number,
        reported_post_type: ""
      };
      report.user_nickname = "ChanYoung"
      report.report_contents = this.report_contents;
      report.reported_post = this.form.id;
      report.reported_post_type = "owner"
      // this.$http.post(`http://202.30.31.91:8000/api/reports/create`, {
      axios.post(`http://202.30.31.91:8000/api/reports/create`, {
      user_nickname : report.user_nickname,
      report_contents : report.report_contents,
      reported_post : report.reported_post,
      reported_post_type : report.reported_post_type
      })
      .then(res => {
        console.log(res.data);
        console.log("ZXCZXC");

      });
      this.contents = "";
      this.getBoardDetail();
    },


    checkFormValidity() {
        const valid = this.$refs.form.checkValidity()
        this.nameState = valid ? 'valid' : 'invalid'
        return valid
    },
    resetModal() {
        this.name = ''
        this.nameState = null
    },
    handleOk(bvModalEvt) {
        // Prevent modal from closing
        bvModalEvt.preventDefault()
        // Trigger submit handler
        this.handleSubmit()
    },
    handleSubmit() {
        // Exit when the form isn't valid
        if (!this.checkFormValidity()) {
          return
        }
        // Push the name to submitted names
        this.submittedNames.push(this.name)
        // Hide the modal manually
        this.$nextTick(() => {
          this.$refs.modal.hide()
          this.createReport()
        })
    }
  }
};
</script>

<style>
.div_header {
  text-align: center;
}
div.board_back_color {
  display: inline-block;
  background-color: white;
  width: 850px;
  margin-top: 50px;
  padding: 20px 20px 50px;
}
div.in_board-view {
  text-align: left;
  display: inline-block;
}

hr.horizontal {
  border: thin dotted gray;
  height: 0px;
  width: 750px;
  border-color: lightgrey;
}

p.comment_date {
  display: inline;
  color: darkgrey;
}

p.comment {
  display: inline;
}

p.comment_name {
  display: inline;
  font-weight: bold;
}

div.comment {
  padding-top: 10px;
}

div.comment_submit {
  padding-top: 20px;
  padding-left: 700px;
}

.comment_input {
  width: 800px;
}

p.report_date {
  display: inline;
  color: darkgrey;
}

p.report {
  display: inline;
}

p.report_name {
  display: inline;
  font-weight: bold;
}

div.report {
  padding-top: 10px;
}

div.report_submit {
  padding-top: 20px;
  padding-left: 700px;
}

.report_input {
  width: 800px;
}
</style>
