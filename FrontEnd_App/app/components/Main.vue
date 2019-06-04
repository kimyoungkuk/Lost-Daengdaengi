<template>
    <Page>
        <ActionBar class="font-weight-bold" title="Lost Daengdaengi">
          <NavigationButton icon = "~/assets/images/baseline_menu_black_18dp.png"/>
        </ActionBar>
                <ScrollView>
          <StackLayout>     
            <WebView scaleY="1" row="0" @loadFinished="completeLoading" height="300" loaded="onWebViewLoaded" id="myWebView" :src="this.$store.state.API_WEBVIEW_URL"/>
            <Progress color="#FA7268" v-show="loadingComplete" :value="loadingValue" row ="0"/>
            <Button class="fab mybtn btn-active" :text="'\uf1a3' + ' 시작하기'" height="50" width="175" @tap="$goto('login')" />
                      <FlexboxLayout flexDirection="column" backgroundColor="#3c495e">
                        <Label text="" height="100" backgroundColor="#FFFFFF"/>
  
  <Label class="fa" height="40" backgroundColor="#FFFFFF" textWrap="true" style="text-align:center">
    <FormattedString>
      <Span class="font-italic font-weight-bold" text="2019 Capstone Design" style="font-size: 24px; color: #FA7268; "/>
    </FormattedString>
  </Label>
    <Label height="30" backgroundColor="#FFFFFF" textWrap="true" style="text-align:center">
    <FormattedString>
      <Span text="Team - Bohemian capsody" fontWeight="bold" style="font-size: 18px; color: #FA7268;"/>
    </FormattedString>
    </Label>
      <Label height="30" backgroundColor="#FFFFFF" textWrap="true" style="text-align:center ">
    <FormattedString>
      <Span text="김영국 | 박신혁 | 박찬영 | 최순원" style="font-size: 16px; background-color:#FA7268; color: #FFFFFF;"/>
    </FormattedString>
  </Label>
  </FlexboxLayout>
          </StackLayout>

               </ScrollView>
               
    </Page>
</template>

<script >
  export default {
    data() {
      return {
        loadingValue: 0,
        loadingComplete: true
        // msg: 'Lost Daengdaengi!'
      }
    },
    methods:{
      completeLoading(){
        this.loadingComplete=false
      },
      OnInit() {
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
@import '~nativescript-theme-core/css/ruby.css';
	.page {
		align-items: center;
		flex-direction: column;
  }
    ActionBar {
        background-color: #FA7268;
        color: #ffffff;
    }

    .mybtn{
      color: #ffffff;
      background-color: #FA7268;
    }

    .message {
        vertical-align: center;
        text-align: center;
        font-size: 20;
        color: #333333;
    }
</style>
