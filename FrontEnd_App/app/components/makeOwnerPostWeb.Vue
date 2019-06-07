<template>
    <Page @loaded="loaded" actionBarHidden="true">
              <ScrollView>
                <StackLayout>  
            <WebView row="0" height="900" @loadFinished="completeLoading" id="myWebView" :src="this.src"/>
            </StackLayout>  
            </ScrollView>
    </Page>
</template>

<script >
var webViewModule = require('ui/web-view');

function gup( name, url ) {
    if (!url) url = location.href;
    name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+name+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( url );
    return results == null ? null : results[1];
}

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
    webView.android.getSettings().setDisplayZoomControls(false);
    webView.android.getSettings().setBuiltInZoomControls(false);
},
      completeLoading(args){
        this.loadingComplete=false
          console.log("--------------------------")
       var query = gup('action', args.url)
       console.log("query : " + query)
        if(query == 'done'){
          console.log("if ok")
          this.$goto("map")
        }
      },
      OnInit() {
          this.src = this.$store.state.API_WEBVIEW_URL + "/ownerForm" + "?user_key=" + this.user_key +"&user_nickname=" +this.user_nickname + "&lat=" + this.lat +"&lng=" + this.lng
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
