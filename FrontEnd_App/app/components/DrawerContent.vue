<template lang="html">
  <ScrollView @swipe = "onSwipe">
    <StackLayout width="100%">
      <Label class="drawer-header" :text="this.$store.state.user_nick_visible"/>

      <Label
        v-for="(page, i) in pages"
        @tap="goToPage(page.component)"
        class="drawer-item"
        :text="page.name"
        :key="i"
      />

      <Button class="drawer-close-button" @tap="closeDrawer()">Close Drawer</Button>
    </StackLayout>
  </ScrollView>
  
</template>

<script>
import sideDrawer from '~/mixins/sideDrawer'
const SwipeDirection = require("tns-core-modules/ui/gestures").SwipeDirection;
export default {
  mixins: [sideDrawer],
  data () {
    return {
      user_NickName : this.$store.state.user_nick_visible,
      user_email :this.$store.state.user_Email,
      
      pages: [
        { name: '마이 페이지', component: this.$router.mypage },
        { name: '내가 쓴 게시물', component: this.$router.PageOne },
//{ name: '로그아웃', component: this.$router.PageTwo }
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