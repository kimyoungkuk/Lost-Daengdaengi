<template>
<div>
  <b-card
    title="전단지를 완성했습니다."
    :img-src="this.src"
    img-alt="Image"
    img-top
    tag="article"
    class="mb-2"
  >
    <b-card-text>
      작성하신 게시글 내용을 기반으로 포스터를 제작했습니다.</br>사용하시려면 받을 이메일을 입력해 주세요.
    </b-card-text>
  </b-card>
  <div>
     <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-1"
          v-model="email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    </div>
</div>
</template>

<script>
  export default {
    data() {
      return {
        src: this.$store.state.posterurl,
        email: '',
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
                   this.$http.post('http://202.30.31.91:8000/api/poster_email',{
                       email : this.email,
                       posterid: this.$store.state.posterid
           }).then(res => {
                console.log(res.data)
                alert("제작된 전단지를 메일로 보냈습니다.")
                this.$router.push("/SubmitPage");
           })
        },
      onReset(evt) {
        evt.preventDefault()
        alert("전단지를 받지 않고 이동합니다.")
        this.$router.push("/SubmitPage");
      }
    }
  }
</script>
