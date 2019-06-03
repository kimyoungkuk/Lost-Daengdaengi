<template>
	<Page class="page">
		<ActionBar title="환영합니다." class="action-bar"/>
		<ScrollView>
			<StackLayout class="home-panel">
				<Label textWrap="true" class="body m-20" text="세계 최강 유기견 찾기 앱입니다."
				/>
				<Button class="btn btn-primary" text="닉네임 입력" @tap="prompt" />
			</StackLayout>
		</ScrollView>
	</Page>
</template>

<script>
const {prompt, inputType } = require("tns-core-modules/ui/dialogs");
export default {
  methods: {
    prompt() {
      prompt({
        title: "닉네임을 입력하세요",
        message: "다른 사용자가 볼 수 있는 ID입니다.",
        okButtonText: "등록",
        cancelButtonText: "취소",
        defaultText: "",
        key: "",
        inputType: inputType.email
      }).then((result) => {
        // The result property is true if the dialog is closed with the OK button, false if closed with the Cancel button or undefined if closed with a neutral button.
        console.log("Dialog result: " + result.result);
        console.log("Text: " + result.text);
            this.$http.post(this.$store.state.API_BACKEND_URL + '/api/users/signUp',{
              key: this.$store.state.user_Email,
              nickname: result.text
                })
                .then(function(response){
                    console.log(response)
                    if(response.status == '201'){
                      if(response.data.state == '0'){
                        // this.$store.state.user_nickname = result.text
                        // console.log(result.text)
                        this.$store.state.user_nickname = response.data.nickname
                        console.log(result.text)
                        this.$goto('map')
                      }
                      else if(response.data.state == '1'){
                        //같은 닉네임의 유저가 이미 있을때
                        alert('닉네임이 중복되었습니다. 다시 입력하세요')
  .then(() => {
    console.log("Alert dialog closed.");
  });
                      }

                    }else{

                    }
                }.bind(this))
                .catch(error => {console.log(error)});
      })
    },
  },
};
</script>

<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
.home-panel{
    font-size: 20;
    margin: 15;
}
</style>