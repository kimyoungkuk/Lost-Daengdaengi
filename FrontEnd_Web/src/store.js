import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user_key: "",
    user_nickname: "",
    user_nick_visible : "로그인이 필요합니다.",
    API_BACKEND_URL: "http://202.30.31.91:8000",
    API_WEBVIEW_URL: "http://202.30.31.91",
    shelter_List : [],
    shelter_List_Near :[],
    CurrentPostType : true,
    ownerPost: {
      title : " ",
      dog_name : " ",
      lost_time : " ",
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
    title : " ",      // 입력 : FinderForm1
    dog_type :" ",    
    dog_feature:" ",  // 입력 : FinderForm5
    phone_num:" ",    // 입력 : FinderForm2
    image:"",         // 입력 : FinderForm6
    lat: 0,
    lng: 0,
    find_time :" ",   // 입력 : FinderForm3
    posted_time:" ",
    posted_due:" ",   // 입력 : FinderForm4
    shelter_name:"대전광역시 동물보호센터"  // 입력 : FinderForm7
  },
},
});
