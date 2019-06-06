import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user_key: " ",
    user_nickname: "Guest",
    user_nick_visible : "로그인이 필요합니다.",
    API_BACKEND_URL: "http://202.30.31.91:8000",
    API_WEBVIEW_URL: "http://202.30.31.91",
    shelter_List : [],
    shelter_List_Near :[],
    CurrentPostType : true,
    ownerPost: {
      title : " ",      // 입력 : OwnerForm1
      dog_name : " ",   // 입력 : OwnerForm5
      lost_time : " ",  // 입력 : OwnerForm3
      dog_sex : 1,      // 입력 : OwnerForm6
      dog_type :" ",    // 입력 : OwnerForm7
      dog_age : 0,      // 입력 : OwnerForm8
      dog_feature:" ",  // 입력 : OwnerForm9
      remark:" ",       // 입력 : OwnerForm11
      phone_num:" ",    // 입력 : OwnerForm2
      image:"default",        // 입력 : OwnerForm10
      lat: 0,
      lng: 0,
      posted_time:"1980-01-01 00:00:00.000000",
      posted_due:" ",   // 입력 : OwnerForm4
  },
    FinderPost: {
    title : "",      // 입력 : FinderForm1
    dog_type :"a",    
    dog_feature:"",  // 입력 : FinderForm5
    phone_num:"",    // 입력 : FinderForm2
    image:"default",         // 입력 : FinderForm6
    lat: 0,
    lng: 0,
    find_time :"",   // 입력 : FinderForm3
    posted_time:"1980-01-01 00:00:00.000000",
    posted_due:"",   // 입력 : FinderForm4
    shelter_name:"대전광역시 동물보호센터"  // 입력 : FinderForm7
  },
},
});
