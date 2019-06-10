<template>
    <Page @loaded="loaded" actionBarHidden="true">
              <ScrollView @loaded="scrloaded">
                <StackLayout>  
                <WebView id="myWebView" @loadFinished="completeLoading"  :src="this.src"/>
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
        height : "auto",
        scrview : null
      }
    },
    methods:{     
      scrloaded(args){
          this.scrview = args.object;
          console.log(this.scrview.height)
      }, 
      loaded(args) {
          const page = args.object;
          const webView = page.getViewById('myWebView')
          webView.android.getSettings().setDisplayZoomControls(false);
          webView.android.getSettings().setBuiltInZoomControls(false);
      },
      completeLoading(args){
        this.src = args.object.src
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
