<template>
    <v-flex class="in_board-view">
      <b-card-group deck>
        <b-card header-tag="header" footer-tag="footer">
          <h6 slot="header" class="mb-0">
            <b-badge variant="dark">작성자</b-badge>
            {{this.form.writer}}
            <b-badge variant="dark">찾은 날짜</b-badge>
            {{this.form.find_time}}
            <b-badge variant="dark">조회수</b-badge>
            {{this.form.count}}
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
                      <span>보호소 : {{this.form.shelter_name}}</span>
                    </div>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn flat color="orange">Share</v-btn>
                    <v-btn flat color="orange">Explore</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </div>
          <h6 slot="footer" v-for="item in form.comments" v-bind:key="item._id">
            <p class="comment_name">{{item.name}}</p>&emsp;
            <p class="comment_date">{{item.createAt}}</p>
            <div class="comment">
              <p class="comment">{{item.memo}}</p>
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
            v-model="memo"
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
      </b-button-group>
      </v-flex>
    </v-flex>
  
</template>

<script>
export default {
  name: "boardView",
  data() {
    return {
      form: {
        _id: this.$route.params.id,
        id: "",
        title: "",
        imageurl: "",
        find_time: "",
        count: "",
        dog_type: "",
        dog_feature: "",
        phone_num: "",
        shelter_name: "",
        comments: [
          {
            name: "",
            memo: "",
            createAt: new Date()
          }
        ]
      },
      memo: "",
      userId: "",
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
          console.log(res.data);
          this.form = res.data[0];
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
      this.$router.push("/board");
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
        name: "",
        memo: "",
        boardId: Number
      };
      comment.name = this.$cookies.get("nickname");
      comment.memo = this.memo;
      comment.boardId = this.form._id;
      this.$http.post(`/api/board/comment`, comment);
      this.memo = "";
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
</style>
