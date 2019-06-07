<template>
    <v-flex class="in_board-view">
      <b-card-group deck>
        <b-card header-tag="header" footer-tag="footer">
          <h6 slot="header" class="mb-0">
            <b-badge variant="dark">작성자</b-badge>
            {{this.form.user_nickname}}
            <b-badge variant="dark">잃어버린 날짜</b-badge>
            {{this.form.lost_time}}
            <b-badge variant="dark">조회수</b-badge>
            {{this.form.view_count}}
            <br>
            <b-badge variant="dark">제목</b-badge>
            {{this.form.title}}
            <b-badge variant="dark">견종</b-badge>
            {{this.form.dog_type}}
          </h6>
          <div>
            <v-layout>
              <v-flex xs12 sm6 offset-sm3>
                <v-card>
                  <v-img class="white--text" height="300px" :src="this.form.imageurl">
                    <v-container fill-height fluid>
                      <v-layout fill-height>
                        <v-flex xs12 align-end flexbox>
                          <span class="headline">{{this.form.dog_type}}</span>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-img>
                  <v-card-title>
                    <div>
                      <span class="grey--text">연락처 : {{this.form.phone_num}}</span>
                      <br>
                      <span>특징 : {{this.form.dog_feature}}</span>
                      <br>
                      <span>비고 : {{this.form.remark}}</span>
                    </div>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn flat color="orange" v-b-modal.modal-finish>Finish</v-btn>
                    <v-btn flat color="orange" v-on:click="recommend">Explore</v-btn>
                    <v-btn flat color="orange" v-b-modal.modal-report v-on:click="reportBoard">report</v-btn>
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
          v-b-modal.modal-delete
          variant="danger"
        >삭제</b-button>
      </b-button-group>
      </v-flex>


      <b-modal
        id="modal-delete"
        ref="modal"
        title="정말로 삭제하실건가요?"
        @show="resetModal"
        @hidden="resetModal"
        @ok="handleOk"
        hide-footer
      >
        
          <b-button
          v-if="userId == form.userId || admin === 1"
          v-on:click="deleteBoard"
          variant="danger"
        >삭제</b-button>
        <b-button
          @click="$bvModal.hide('modal-delete')"
        >취소</b-button>
      </b-modal>

      <b-modal
        id="modal-finish"
        ref="modal"
        title="정말로 유기견이 반환되었나요?"
        @show="resetModal"
        @hidden="resetModal"
        @ok="handleOk"
        hide-footer
      >
          <b-button
          v-if="userId == form.userId || admin === 1"
          v-on:click="finishBoard"
          variant="danger"
        >예</b-button>
        <b-button
          @click="$bvModal.hide('modal-finish')"
        >아니요</b-button>
      </b-modal>


      <b-modal
        id="modal-report"
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
      key :  this.$store.state.user_key,
      nickname :  this.$store.state.user_nickname,
      lat : 0,
      lng : 0,
      name: '',
      nameState: null,
      submittedNames: [],
        
      form: {
        _id: this.$route.params.id,
        id: "",
        title: "",
        imageurl: "",
        lost_time: "",
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
    console.log("TTT")
    let urlParams = new URLSearchParams(window.location.search);
    console.log(urlParams.get('key'))
    console.log(urlParams.get('nickname'))
    console.log("TTT")
    this.$store.state.user_key = urlParams.get('key');
    this.key = urlParams.get('key');
    this.$store.state.user_nickname = urlParams.get('nickname');
    this.nickname = urlParams.get('nickname');
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
          `http://202.30.31.91:8000/api/ownerPosts/detail/${
            this.$route.params.id
          }`
        )
        .then(res => {
          console.log(res.data.post[0]);
          console.log(res.data.comments)
          this.form = res.data.post[0];
          this.comments = res.data.comments
          console.log(this.form);
          this.form.lost_time = this.$moment(this.form.lost_time).format(
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
      
      console.log("!@#")
      console.log(this.form.user_nickname)
      if(this.form.user_nickname==this.nickname){

        this.$http
        .post(`http://202.30.31.91:8000/api/ownerPosts/delete/${this.$route.params.id}`)
        .then(res => {
          const status = res.status;
          // if (status === 200) {
            alert("정상적으로 삭제되었습니다.");
            this.$router.push("/ownerboard");
          // } else if (status === 203) {
          //   alert("해당 권한이 존재하지 않습니다.");
          //   this.$router.push("/board");
          // }
        })
        .catch(err => {
          alert(err);
        });
      }
      else{
        alert("해당 권한이 존재하지 않습니다.");
        this.$router.push("/ownerboard");
      }
    },
    finishBoard(){
      this.$router.push(`/ownerboard/finish/${this.$route.params.id}`);
      if(this.form.user_nickname==this.nickname){

        this.$http
        .post(`http://202.30.31.91:8000/api/ownerPosts/finish/${this.$route.params.id}`)
        .then(res => {
          const status = res.status;
            this.$router.push("/ownerboard");
        })
        .catch(err => {
          alert(err);
        });
      }
      else{
        alert("해당 권한이 존재하지 않습니다.");
        this.$router.push("/ownerboard");
      }

    },
    toBoard() {
      this.$router.push("/ownerboard");
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
    addComment() {
      let comment = {
        user_key: "",
        user_nickname: "",
        contents: "",
        commented_post: Number,
        commented_post_type: ""
      };
      comment.user_key = this.key;
      comment.user_nickname = this.nickname;
      comment.contents = this.contents;
      comment.commented_post = this.form.id;
      comment.commented_post_type = "owner"
      // this.$http.post(`http://202.30.31.91:8000/api/comments/create`, {
      axios.post(`http://202.30.31.91:8000/api/comments/create`, {
      user_key : this.$store.state.user_key,
      user_nickname : this.$store.state.user_nickname,
      contents : this.contents,
      commented_post : this.form.id,
      commented_post_type : "owner"
      })
      .then(res => {
        console.log(res.data);
        console.log("QWEQWE");
        this.$router.push(`/ownerboard/view/${this.$route.params.id}`);
        // this.getBoardDetail();
      });
      this.contents = "";
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
    recommend(){
      this.$router.push(`/ownerboard/recommend/${this.$route.params.id}`);


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
