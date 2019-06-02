
export default {
    data () {
      return {
        nickname : "",
        // we'll use this to enable gestures on our sideDrawer.
        gesturesEnabled: false
      }
    },
    computed: {
      // drawerElement points to the drawer node using vue $refs
      drawerElement () { return (this.$refs && this.$refs.drawer) || null },
      // drawer is responsible for getting and setting the sideDrawer property in vuex state.
      drawer: {
        get () { return this.$store.getters.sideDrawer },
        set (v) { return this.$store.commit('setSideDrawer', v) }
      }
    },
    watch: {
      // we watch the drawer prop for changes and open/close the sideDrawer accordingly
      drawer (v) {
        if (this.drawerElement) {
          return v ?
            this.drawerElement.nativeView.showDrawer() :
            this.drawerElement.nativeView.closeDrawer()
        }
      }
    },
    methods: {
      // some helpful methods for opening and closing the drawer from the vue instance.
      openDrawer () {
        this.$store.state.user_nick_visible = this.$store.state.user_nickname + ' 님 안녕하세요'
        this.drawer = true
      },
      closeDrawer () {
        console.log(this.$store.state.user_nickname)
        this.drawer = false
      }
    }
  }