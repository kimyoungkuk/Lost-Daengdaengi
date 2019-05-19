<template>
    <Page>
        <ActionBar title="Lost DaengDaengi Main"/>
                <ScrollView>
          <StackLayout>
            <!-- <Image class="logo" src="~/assets/images/DaengDaengi.png" horizontalAlignment="center" stretch="none"/> -->
            <WebView row="1" height="440" loaded="onWebViewLoaded" id="myWebView" src="http://192.168.43.210:8080/" />
            <Button class="btn btn-primary" text="시작하기" height="50" width="175" @tap="$goto('login')" />
            <!-- <Label class="message" :text="msg" col="0" row="0"/> -->
          </StackLayout>
               </ScrollView>
    </Page>
</template>

<script >

  export default {
    data() {
      return {
        // msg: 'Lost Daengdaengi!'
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
