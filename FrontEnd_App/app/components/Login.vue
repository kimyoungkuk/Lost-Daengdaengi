<template>
	<Page actionBarHidden="true">
        <GridLayout row="auto, auto,auto">
		<FlexboxLayout class="page">
			<StackLayout class="form">
				<Image class="logo" src="~/assets/images/DaengDaengi.png" />
				<Label class="header" text="Lost DaengDaengi" />
                <Button v-show="isLoggingIn" :text="'\uf1a0' + ' Google login'" :isEnabled="!processing" @tap="loginGoogle" class="fab mybtn btn-active" />
			</StackLayout>
		</FlexboxLayout>
        <ActivityIndicator rowSpan="3" height="50" color="#FA7268" :busy="processing"></ActivityIndicator>
        </GridLayout>
	</Page>
</template>

<script>
// A stub for a service that authenticates users.

import firebase from "nativescript-plugin-firebase";

const userService = {
    async loginGoogle(user) {
     await firebase
      .login({
        type: firebase.LoginType.GOOGLE       
      })
      .then(result => {
          console.log("***********************")
          console.log(result)
          user.user.email = result.email
          user.key = result.uid
        return Promise.resolve(JSON.stringify(result));
      })
      .catch(error => {
        console.error(error);
        return Promise.reject(error);
      });
  },
  async register(user) {
    return await firebase.createUser({
      email: user.email,
      password: user.password
    });
  },
  async login(user) {
    return await firebase.login({
      type: firebase.LoginType.PASSWORD,
      passwordOptions: {
        email: user.email,
        password: user.password
      }
    });
  },
  async resetPassword(email) {
    return await firebase.resetPassword({
      email: email
    });
  }
};

export default {
    data() {
        return {
            isLoggingIn: true,
            key: ' ',
            isUser: ' ',
            user: {
                email: "",
                password: "",
                confirmPassword: ""
            },
            processing: false,
        };
    },
    methods: {
        loginGoogle(){
        this.processing = true;
        userService
        .loginGoogle(this)
        .then((result) => {
          console.log('----Gmail 유저 이메일----')
          console.log(this.user.email)
          console.log(this.key)
          this.$store.state.user_key = this.key
          this.$http.post(this.$store.state.API_BACKEND_URL + '/api/users/login',{
              key: this.key
                })
                .then(function(response){
                    console.log(response)
                    if(response.data.state == '1'){
                        this.$store.state.user_nickname = response.data.nickname
                        console.log(response.data)
                        this.$goto('portal');
                        this.processing = false;
                    }
                    else if(response.data.state == '0'){
                        this.$goto('setUserInfo')
                        this.processing = false;
                    }
                }.bind(this))
                .catch(error => {console.log(error)});
        })
        .catch((error) => {
          console.error(err);
          this.alert(error)
        });
    },

        login() {
            userService
                .login(this.user)
                .then(() => {
                    console.log('----로그인 시 받아온 값----')
                    console.log(this.user.email)
                    this.$goto('map');  
                })
                .catch(() => {
                    this.alert("Unfortunately we could not find your account.");
                });
        },
    }
};
</script>

<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
	.page {
		align-items: center;
		flex-direction: column;
	}

      .mybtn{
      color: #ffffff;
      background-color: #FA7268;
    }
	.form {
		margin-left: 30;
		margin-right: 30;
		flex-grow: 2;
		vertical-align: middle;
	}

	.logo {
		margin-bottom: 12;
		height: 90;
		font-weight: bold;
	}

	.header {
		horizontal-align: center;
		font-size: 25;
		font-weight: 600;
		margin-bottom: 50;
		text-align: center;
		color: #FA7268;
	}

	.input-field {
		margin-bottom: 25;
	}

	.input {
		font-size: 18;
		placeholder-color: #A8A8A8;
	}

	.input-field .input {
		font-size: 54;
	}

	.btn-primary {
		height: 50;
		margin: 30 5 15 5;
		background-color: #4ba5fa;
		border-radius: 5;
		font-size: 20;
		font-weight: 600;
	}

	.login-label {
		horizontal-align: center;
		color: #A8A8A8;
		font-size: 16;
	}

	.sign-up-label {
		margin-bottom: 20;
	}

	.bold {
		color: #000000;
	}
</style>
