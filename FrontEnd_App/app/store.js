import Vue from 'nativescript-vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user_key: "",
    user_nickname: "",
    user_nick_visible : "로그인이 필요합니다.",
    API_BACKEND_URL: "http://202.30.31.91:8000",
    API_WEBVIEW_URL: "http://202.30.31.91",
    Redirect_URL: "",
    // API_WEBVIEW_URL: "http://192.168.43.210:8080",
    shelter_List : [],
    shelter_List_Near :[],
    CurrentPostType : true,
    imageAsset: '',
    ownerPost: {
      title : "x",
      dog_name : "x",
      lost_time : "1111-11-11 00:00",
      dog_sex : 1,
      dog_type :"x",
      dog_age : 1,
      dog_feature:"x",
      remark:"x",
      phone_num:"x",
      image:"x",
      lat: 0,
      lng: 0,
      posted_time:"1111-11-11 00:00:00",
      posted_due:"1111-11-11",
  },
  FinderPost: {
    title : "x",
    dog_type :"x",
    dog_feature:"x",
    phone_num:"x",
    image:"x",
    lat: 0,
    lng: 0,
    find_time :"1111-11-11 00:00",
    posted_time:"1111-11-11 00:00:00",
    posted_due:"1111-11-11",
    shelter_name:"x"
  },
  sideDrawer: false,
  selected_loc : ""
},
  mutations: {
    setSideDrawer (state, data) {
      state.sideDrawer = data
    }
  },
  actions: {

  },
  getters :{
    sideDrawer: (state) => state.sideDrawer
  }
});
