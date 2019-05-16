<template>
	<Page>
		<FlexboxLayout class="page">
			<StackLayout class="form">
				<Image class="logo" src="~/assets/images/DaengDaengi.png" />
				<Label class="header" text="Lost DaengDaengi" />

				<StackLayout class="input-field" marginBottom="25">
					<TextField class="input" hint="Email" keyboardType="email" autocorrect="false" autocapitalizationType="none" v-model="user.email"
					 returnKeyType="next" @returnPress="focusPassword" fontSize="18" />
					<StackLayout class="hr-light" />
				</StackLayout>

				<StackLayout class="input-field" marginBottom="25">
					<TextField ref="password" class="input" hint="Password" secure="true" v-model="user.password" :returnKeyType="isLoggingIn ? 'done' : 'next'"
					 @returnPress="focusConfirmPassword" fontSize="18" />
					<StackLayout class="hr-light" />
				</StackLayout>

				<StackLayout v-show="!isLoggingIn" class="input-field">
					<TextField ref="confirmPassword" class="input" hint="Confirm password" secure="true" v-model="user.confirmPassword" returnKeyType="done"
					 fontSize="18" />
					<StackLayout class="hr-light" />
				</StackLayout>

				<Button :text="isLoggingIn ? 'Log In' : 'Sign Up'" @tap="submit" class="btn btn-primary m-t-20" />
                <Button v-show="isLoggingIn" :text="'\uf1a0' +' Google login' " @tap="loginGoogle" class="fab btn btn-active" />
				<Label v-show="isLoggingIn" text="Forgot your password?" class="login-label" @tap="forgotPassword" />
			</StackLayout>

			<Label class="login-label sign-up-label" @tap="toggleForm">
	          <FormattedString>
	            <Span :text="isLoggingIn ? 'Don’t have an account? ' : 'Back to Login'" />
	            <Span :text="isLoggingIn ? 'Sign up' : ''" class="bold" />
	          </FormattedString>
	        </Label>
		</FlexboxLayout>
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

// A stub for the main page of your app. In a real app you’d put this page in its own .vue file.
const HomePage = {
    template: `
<Page>
	<Label class="m-20" textWrap="true" text="You have successfully authenticated. This is where you build your core application functionality."></Label>
</Page>
`
};

export default {
    data() {
        return {
            isLoggingIn: true,
            key: ' ',
            user: {
                email: "ID@gmail.com",
                password: "Password",
                confirmPassword: "Password"
            }
        };
    },
    methods: {
        loginGoogle(){
        userService
        .loginGoogle(this.user)
        .then((result) => {
          console.log('----로그인 시 받아온 값----')
          console.log(this.user.email)
          this.axios.get('http://210.107.198.174:8000/LDapp/dog_shelter_list', {
              
          }).then(res => {console.log(res.data)})

          this.axios.post('http://081a1720.ngrok.io/api/users/login',{
              key: this.user.email
                })
                .then(function(response){
                    console.log(response)
                    console.log("보냄")
                })
                .catch(error => {console.log(error)});
                this.$goto('map');  
        })
        .catch((error) => {
          console.error(err);
          this.alert(error)
        });
    },
        toggleForm() {
            this.isLoggingIn = !this.isLoggingIn;
        },

        submit() {
            if (!this.user.email || !this.user.password) {
                this.alert(
                    "Please provide both an email address and password."
                );
                return;
            }
            if (this.isLoggingIn) {
                this.login();
            } else {
                this.register();
            }
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

        register() {
            var validator = require("email-validator");
      if (!validator.validate(this.user.email)) {
        this.alert("Please enter a valid email address.");
        return;
      }
            if (this.user.password != this.user.confirmPassword) {
                this.alert("Your passwords do not match.");
                return;
            }

            userService
                .register(this.user)
                .then(() => {
                    this.alert("Your account was successfully created.");
                    this.isLoggingIn = true;
                })
                .catch(() => {
                    this.alert(
                        "Unfortunately we were unable to create your account."
                    );
                });
        },

        forgotPassword() {
            prompt({
                title: "Forgot Password",
                message:
                    "Enter the email address you used to register for APP NAME to reset your password.",
                inputType: "email",
                defaultText: "",
                okButtonText: "Ok",
                cancelButtonText: "Cancel"
            }).then(data => {
                if (data.result) {
                    userService
                        .resetPassword(data.text.trim())
                        .then(() => {
                            this.alert(
                                "Your password was successfully reset. Please check your email for instructions on choosing a new password."
                            );
                        })
                        .catch(() => {
                            this.alert(
                                "Unfortunately, an error occurred resetting your password."
                            );
                        });
                }
            });
        },

        focusPassword() {
            this.$refs.password.nativeView.focus();
        },
        focusConfirmPassword() {
            if (!this.isLoggingIn) {
                this.$refs.confirmPassword.nativeView.focus();
            }
        },

        alert(message) {
            return alert({
                title: "APP NAME",
                okButtonText: "OK",
                message: message
            });
        }
    }
};
</script>

<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
	.page {
		align-items: center;
		flex-direction: column;
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
		margin-bottom: 70;
		text-align: center;
		color: #D51A1A;
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
		background-color: #D51A1A;
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
