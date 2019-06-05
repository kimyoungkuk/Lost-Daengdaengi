<template>
    <Page actionBarHidden="true">
           <!-- <FlexboxLayout flexDirection="column" backgroundColor="#3c495e"> -->
            <!-- <Image class="logo" src="~/assets/images/DaengDaengi.png" horizontalAlignment="center" stretch="none"/> -->
            <GridLayout rows = "*,auto">
            <WebView row="0" @loadFinished="completeLoading" loaded="onWebViewLoaded" id="myWebView" :src="this.src"/>
            <Progress row="1" color="#4ba5fa" v-show="loadingComplete" :value="loadingValue"/>
            </GridLayout>
            <!-- <Label class="message" :text="msg" col="0" row="0"/> -->      
  <!-- </FlexboxLayout> -->
          

               
               
    </Page>
</template>

<script >
var webViewModule = require('ui/web-view');
  export default {
    data() {
      return {
        loadingValue: 0,
        loadingComplete: true,
        src: ' ',
        user_key: this.$store.state.user_Email,
        user_nickname: this.$store.state.user_nickname,
        lat: this.$store.state.FinderPost.lat,
        lng: this.$store.state.FinderPost.lng,
      }
    },
    methods:{
            loaded(args) {
    const page = args.object;
    this.webView = page.getViewById('myWebView')
    debugger;
    //webView.url = 
    this.webView.on(webViewModule.WebView.loadFinishedEvent, function (args) {
        console.log(JSON.stringify(args.url));
    });
},
      completeLoading(args){
        this.loadingComplete=false
        args.object.android.getSettings().setBuiltInZoomControls(false);
      },
      OnInit() {
          this.src = this.$store.state.API_WEBVIEW_URL + "/finderForm"+ "?user_key=" + this.user_key +"&user_nickname=" +this.user_nickname + "&lat=" + this.lat +"&lng=" + this.lng
          console.log(this.src)
    var d = setInterval(() => {
      this.loadingValue += 1
      if(this.loadingValue==90){
        clearInterval(d)
      }
    }, 20);

}

    },
    created(){
      this.OnInit()
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
