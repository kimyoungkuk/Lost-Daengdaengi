<template>
    <Page @loaded="loaded" actionBarHidden="true">
              <ScrollView>
                <StackLayout>  
                <WebView id="myWebView" row="0" @loadFinished="completeLoading"  :src="this.src"/>
                <Progress row="1" color="#FA7268" v-show="loadingComplete" :value="loadingValue"/>
              </StackLayout>  
            </ScrollView>
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
        user_key: this.$store.state.user_key,
        user_nickname: this.$store.state.user_nickname,
        lat: this.$store.state.FinderPost.lat,
        lng: this.$store.state.FinderPost.lng,
      }
    },
    methods:{      
      loaded(args) {
          const page = args.object;
          const webView = page.getViewById('myWebView')
    webView.android.getSettings().setJavaScriptEnabled(true);
    webView.android.getSettings().setDisplayZoomControls(false);
    webView.android.getSettings().setBuiltInZoomControls(false);
    webView.android.getSettings().setAllowFileAccessFromFileURLs(true);
    webView.android.getSettings().setAllowUniversalAccessFromFileURLs(true);
    webView.android.getSettings().setMediaPlaybackRequiresUserGesture(false);
    webView.android.getSettings().setUseWideViewPort(true);
    webView.android.getSettings().setDomStorageEnabled(true);
      },
      completeLoading(args){
        this.loadingComplete=false
 
      },
      OnInit() {
          this.src = this.$store.state.Redirect_URL
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
    .message {
        vertical-align: center;
        text-align: center;
        font-size: 20;
        color: #333333;
    }
</style>
