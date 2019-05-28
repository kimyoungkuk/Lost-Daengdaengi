import Vue from 'nativescript-vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user_Email: "",
    API_BACKEND_URL: "http://202.30.31.91:8000",
    API_WEBVIEW_URL: "http://202.30.31.91",
    // API_WEBVIEW_URL: "http://192.168.43.210:8080",
    shelter_List : [],
    shelter_List_Near :[],
    CurrentPostType : true,
    ownerPost: {
      title : " ",
      dog_name : " ",
      lost_time : " ",
      lost_time1 : " ",
      dog_sex : 1,
      dog_type :" ",
      dog_age : 0,
      dog_feature:"",
      remark:" ",
      phone_num:" ",
      image:" ",
      lat: 0,
      lng: 0,
      posted_time:" ",
      posted_due:" ",
  },
  FinderPost: {
    title : " ",
    dog_type :" ",
    dog_feature:" ",
    phone_num:" ",
    image:"",
    lat: 0,
    lng: 0,
    find_time :" ",
    find_time1 : " ",
    posted_time:" ",
    posted_due:" ",
    shelter_name:"대전광역시 동물보호센터"
  },
},
  mutations: {

  },
  actions: {

  }
});