<template>
    <v-flex class="in_board-view">
      <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
      <b-card-group deck>
        <b-card header-tag="header" footer-tag="footer">
          <div class="detailTitle googleFont_finder" slot="header">
            <div id="detailTitle-left">
              <v-btn
              small
              depressed
              right
              router-link to="/finderBoard">
                <v-icon color="#FA7268" left>arrow_back</v-icon>
              </v-btn>
            </div>
            <div id="datailTitle-center"><h5 id="detailTitle1">Lost-Daengdaengi</h5></div>
            <div id="detailTitle-right">조회 : {{this.form.view_count}}</div>
          </div>
          <div class="googleFont_finder">
            <v-layout>
              <v-flex xs12 sm6 offset-sm3>
                <v-card>
                  <v-img class="white--text" height="300px" :src="this.form.imageurl"></v-img>
                  <v-card-title>
                    <div>
                      <h3>
                        <p>
                          <b-badge variant="primary">발견</b-badge>
                          [{{this.form.dog_type}}]
                          {{this.form.title}}
                        </p>
                      </h3>
                      <div style="line-height:2em;">
                        <li>날&nbsp&nbsp짜 : {{this.form.find_time}}</li>
                        <li>특&nbsp&nbsp징 : {{this.form.dog_feature}}</li>
                        <li>닉네임 : {{this.form.user_nickname}}</li>
                        <li>연락처 : {{this.form.phone_num}}</li>
                      </div>
                    </div>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn class="btn btn-primary custom-btn" small="true" color="white" flat v-b-modal.modal-finish>반환 완료</v-btn>
                    <!-- <v-btn class="btn btn-primary custom-btn" small="true" color="white" flat v-on:click="recommend">유기견 찾기</v-btn> -->
                    <v-btn class="btn btn-primary custom-btn" small="true" color="white" flat v-b-modal.modal-report v-on:click="reportBoard">신고</v-btn>
                    <div class="detailDelete-icon" align="right">
                      <v-btn
                      small
                      depressed
                      flat
                      v-b-modal.modal-delete
                      >
                        <i class="material-icons">delete</i>
                      </v-btn>
                    </div>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </div>
          <h6 slot="footer" v-for="item in comments" v-bind:key="item.id">
            <p class="comment_name">{{item.user_nickname}}</p>&emsp;
            <p class="comment_date float-right">{{$moment(item.commented_time).format(
            "LLLL"
          )}}</p>
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

      <v-flex class="googleFont_finder">
        <h4>
          <b-badge>댓글</b-badge>
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
            <b-button class="comment" type="submit" size="sm">댓글 작성(Enter)</b-button>
          </v-flex>
        </b-form>
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
        <b-button class="float-right"
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
        <b-button class="float-right"
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

      <b-modal ref="report-confirm-modal" hide-footer title="신고 접수">
        <div class="d-block text-center">
          <h5>정상적으로 신고가 접수되었습니다.</h5>
        </div>
        <b-button class="mt-3 btn-primary" block @click="hideReportConfirmModal">확인</b-button>
      </b-modal>

      <b-modal ref="delete-success-confirm-modal" hide-footer title="삭제 완료">
        <div class="d-block text-center">
          <h5>정상적으로 삭제되었습니다.</h5>
        </div>
        <b-button class="mt-3 btn-primary" block @click="hideDeleteSuccessConfirmModal">확인</b-button>
      </b-modal>

      <b-modal ref="delete-fail-confirm-modal" hide-footer title="삭제 권한 없음">
        <div class="d-block text-center">
          <h5>권한이 없습니다.</h5>
        </div>
        <b-button class="mt-3 btn-primary" block @click="hideDeleteFailConfirmModal">확인</b-button>
      </b-modal>

      <b-modal ref="finish-success-confirm-modal" hide-footer title="반환 처리 완료">
        <div class="d-block text-center">
          <h5>정상적으로 반환처리되었습니다.</h5>
        </div>
        <b-button class="mt-3 btn-primary" block @click="hideFinishSuccessConfirmModal">확인</b-button>
      </b-modal>

      <b-modal ref="finish-fail-confirm-modal" hide-footer title="반환처리 권한 없음">
        <div class="d-block text-center">
          <h5>권한이 없습니다.</h5>
        </div>
        <b-button class="mt-3 btn-primary" block @click="hideFinishFailConfirmModal">확인</b-button>
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
        find_time: "",
        view_count: "",
        dog_type: "",
        dog_feature: "",
        phone_num: "",
        shelter_name: "",
        user_nickname:"",
      },
      comments: [
          {
            user_key: "",
            user_nickname: "",
            contents: "",
            commented_time: new Date(),
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
    if(this.$store.state.user_nickname=="Guest"){
      this.$store.state.user_key = urlParams.get('key');
      this.$store.state.user_nickname = urlParams.get('nickname');
    }
    this.key = this.$store.state.user_key
    this.nickname = this.$store.state.user_nickname
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

      console.log("!@#")
      console.log(this.form.user_nickname)
      if(this.form.user_nickname==this.nickname){

        this.$http
        .post(`http://202.30.31.91:8000/api/finderPosts/delete/${this.$route.params.id}`)
        .then(res => {
          const status = res.status;
          // if (status === 200) {
            this.$bvModal.hide('modal-delete')
            this.showDeleteSuccessConfirmModal()
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
        this.$bvModal.hide('modal-delete')
        this.showDeleteFailConfirmModal();
      }
    },
    finishBoard(){
      // this.$router.push(`/finderboard/finish/${this.$route.params.id}`);
      if(this.form.user_nickname==this.nickname){

        this.$http
        .post(`http://202.30.31.91:8000/api/finderPosts/finish/${this.$route.params.id}`)
        .then(res => {
          const status = res.status;
            this.$bvModal.hide('modal-finish')
            this.showFinishSuccessConfirmModal()
        })
        .catch(err => {
          alert(err);
        });
      }
      else{
        this.$bvModal.hide('modal-finish')
        this.showFinishFailConfirmModal();
      }

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
      comment.commented_post_type = "finder"
      // this.$http.post(`http://202.30.31.91:8000/api/comments/create`, {
      axios.post(`http://202.30.31.91:8000/api/comments/create`, {
      user_key : this.$store.state.user_key,
      user_nickname : this.$store.state.user_nickname,
      contents : this.contents,
      commented_post : this.form.id,
      commented_post_type : "finder"
      })
      .then(res => {
        console.log(res.data);
        this.contents = "";
        this.getBoardDetail();
      });
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
      this.$router.push(`/finderboard/recommend/${this.$route.params.id}`);


    },
    createReport() {
      let report = {
        user_nickname: "",
        report_contents: "",
        reported_post: Number,
        reported_post_type: ""
      };
      report.user_nickname = this.$store.state.user_nickname
      report.report_contents = this.report_contents;
      report.reported_post = this.form.id;
      report.reported_post_type = "finder"
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
          this.showReportConfirmModal()
        })
    },
    hd(){
      this.$nextTick(() => {
        this.$refs.modal.hide()
      })
    },
    showReportConfirmModal() {
      this.$refs['report-confirm-modal'].show()
    },
    hideReportConfirmModal() {
      this.$refs['report-confirm-modal'].hide()
    },
    showDeleteSuccessConfirmModal() {
      this.$refs['delete-success-confirm-modal'].show()
    },
    hideDeleteSuccessConfirmModal() {
      this.$refs['delete-success-confirm-modal'].hide()
      
      this.$router.push("/finderboard");
    },
    showDeleteFailConfirmModal() {
      this.$refs['delete-fail-confirm-modal'].show()
    },
    hideDeleteFailConfirmModal() {
      this.$refs['delete-fail-confirm-modal'].hide()
    },
    showFinishSuccessConfirmModal() {
      this.$refs['finish-success-confirm-modal'].show()
    },
    hideFinishSuccessConfirmModal() {
      this.$refs['finish-success-confirm-modal'].hide()
      
      this.$router.push("/finderboard");
    },
    showFinishFailConfirmModal() {
      this.$refs['finish-fail-confirm-modal'].show()
    },
    hideFinishFailConfirmModal() {
      this.$refs['finish-fail-confirm-modal'].hide()
    },

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
/* div.in_board-view { */
  /* text-align: left; */
  /* display: inline-block; */
/* } */

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

.detailTitle {
  display: flex;
  /* line-height: %; */
}
#detailTitle1 {
  line-height: 190%;
}

#detailTitle-left {
  flex: 1;
}

#detailTitle-center {
  flex: 3;
  text-align: center;
  line-height: 300%;
}

#detailTitle-right {
  flex: 1;
  text-align: right;
  line-height: 275%;
}

.detailFront{
  float: left;
  width: 100%;
  margin-right: -300px;
  padding-right: 330px;
  box-sizing: border-box;
  text-align: justify;
  text-justify: inter-word;
}

.detailLast{
  float: right;
  width: 300px;
}

.material-icons {
  color: grey;
  flex: 1;
  text-align: right;
}

.detailDelete-icon {
  flex: 1;
}

.detail-btn-left {

}

.detail-btn-right {
  
}
</style>
