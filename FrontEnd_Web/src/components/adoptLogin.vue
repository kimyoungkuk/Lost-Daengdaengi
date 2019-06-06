<template>
<div>
  <b-card bg-variant="light">
    <b-form @submit="onSubmit">
    <b-form-group
      label-cols-lg="3"
      label="Login"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
    >
      <b-form-group
        label-cols-sm="3"
        label="Account:"
        label-align-sm="right"
        label-for="nested-account"
      >
        <b-form-input id="nested-account" v-model="account"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Password"
        label-align-sm="right"
        label-for="nested-pwd"
      >
        <b-form-input id="nested-pwd" type="password" v-model="pwd"></b-form-input>
      </b-form-group>
      
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form-group>
    </b-form>
  </b-card>
</div>
</template>

<script>
  export default {
    data() {
      return {
        account:'',
        pwd:'',
      }
    },
    methods:{
        onSubmit(evt) {
            evt.preventDefault()
            
            this.$http.post('http://202.30.31.91:8000/adopt/login', {
            account:this.account,
            pwd:this.pwd,
            

        }).then(res => {
            
            console.log("QWE")
            console.log(res.data)
            console.log("QWE")
            if(res.data==1){
                this.$store.state.user_nickname=this.account
                this.$store.state.user_key="adopt_admin"
                console.log(this.$store.state.user_key)
                this.$router.push("/adopt/post/list");
            }
            else{
                alert("계정과 비밀번호를 다시 확인해주세요")
            }
            // this.posts = res.data
        })

        }
    }
  }
</script>