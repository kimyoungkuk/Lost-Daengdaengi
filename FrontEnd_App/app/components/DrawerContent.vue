<template lang="html">
 <gridlayout rows = "*,auto">
  <ScrollView  row="0" @swipe = "onSwipe">
   
    <StackLayout width="100%">
      <Label class="drawer-header" backgroundColor= "#FA7268" color = "#ffffff" :text="this.$store.state.user_nick_visible"/>

      <Label
        backgroundColor = "#ffffff"
        color = "#FA7268"
        v-for="(page, i) in pages"
        @tap="goToPage(page.component)"
        class="drawer-item"
        :text="page.name"
        :key="i"
      />

      
    </StackLayout>
   
   
  </ScrollView>
   <Button row="1"class="drawer-close-button" backgroundColor= "#FA7268" color = "#ffffff" @tap="closeDrawer" verticalAlignment="bottom">닫기</Button>
   </gridlayout>
  
</template>

<script>
import sideDrawer from '~/mixins/sideDrawer'
const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
export default {
  mixins: [sideDrawer],
  data () {
    return {
      user_NickName : this.$store.state.user_nick_visible,
      user_key :this.$store.state.user_key,
      
      pages: [
        { name: '마이 페이지', component: this.$router.mypage },
        { name: '내가쓴 게시물', component: this.$router.myPosts },
        { name: '닮은 강아지 찾기', component: this.$router.jamjam }
      ]
    }
  },
  methods: {
    onSwipe(args){
      if(args.direction == SwipeDirection.left){
        this.closeDrawer()
      }
    },
    goToPage (pageComponent) {

      // use the manual navigation method
      this.$navigateTo(pageComponent)
      console.log(this.user_NickName);
      // and we probably want to close the drawer when changing pages
      this.closeDrawer()
    }
  }
}
</script>

<style lang="css">
.drawer-close-button {
  margin-top: 20;
  padding: 10 10 10 10;
  background-color: #53ba82;
  color: #ffffff;
}

.drawer-header {
    padding: 50 16 16 16;
    margin-bottom: 16;
    background-color: #333333;
    color: #ffffff;
    font-size: 24;
}

.drawer-item {
    padding: 8 16;
    color: #333333;
    font-size: 16;
}
</style>