<template>
    <Page>
        <ActionBar android.icon="res://icon" title="Lost DaengDaengi Main"/>
                <ScrollView>
          <StackLayout>
            <!-- <Image class="logo" src="~/assets/images/DaengDaengi.png" horizontalAlignment="center" stretch="none"/> -->
            <WebView row="1" height="440" loaded="onWebViewLoaded" id="myWebView" src="http://192.168.43.210:8080/" />
            <Button class="btn btn-primary" text="시작하기" height="50" width="175" @tap="$goto('login')" />
            <Button text="맵뷰" height="50" width="100" @tap="$goto('map')" />
            <Button text="게시물작성" height="50" width="100" @tap="$goto('makePost')" />
            <Button text="카메라" height="50" width="100" @tap="$goto('camera')" />
            <Button text="imP" height="50" width="100" @tap="$goto('makePost_Finder')" />
            <Button text="닉네임" height="50" width="100" @tap="$goto('setUserInfo')" />
            <Button text="카메라" height="50" width="100" @tap="$goto('makePost')" />
            <Button text="Parallax" height="50" width="100" @tap="$goto('parallax')" />
            <Button text="찾은 게시판" height="50" width="100" @tap="$goto('ownerBoard')" />
            <Button text="찾는 게시판" height="50" width="100" @tap="$goto('finderBoard')" />
            <Button text="GPS" height="50" width="100" @tap="$goto('gps')" />  
            <Label class="message" :text="msg" col="0" row="0"/>
          </StackLayout>
               </ScrollView>
    </Page>
</template>

<script >

  export default {
    data() {
      return {
        msg: 'Lost Daengdaengi!'
      }
    },
    methods:{

    }
  }
</script>

<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
	.page {
		align-items: center;
		flex-direction: column;
  }
    ActionBar {
        background-color: #4ba5fa;
        color: #ffffff;
    }

    .message {
        vertical-align: center;
        text-align: center;
        font-size: 20;
        color: #333333;
    }
</style>
