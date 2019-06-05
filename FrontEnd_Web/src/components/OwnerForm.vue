<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <!-- 1. title -->
        <transition appear name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==1" class="mainOwnerForm">
            <h1 class="googleFont">1. 제목을 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input
                    id="input-2"
                    v-model="title"
                    required
                    placeholder="Enter your title."
                    ></b-form-input>
                </b-form-group>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 2. phone_num -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==2" class="mainOwnerForm">
            <h1 class="googleFont">2. 전화번호를 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input
                    id="input-2"
                    v-model="phone_num"
                    required
                    placeholder="Enter your phone number."
                    ></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 3. lost_time -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==3" class="mainOwnerForm">
            <h1 class="googleFont">3. 잃어버린 시간을 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input id="date-1" v-model="date" required type="date"></b-form-input>
                    <b-form-input id="time-1" v-model="time" required type="time"></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 4. posted_due -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==4" class="mainOwnerForm">
            <h1 class="googleFont">4. 게시 기간을 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input id="date-1" v-model="posted_due" required type="date"></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 5. dog_name -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==5" class="mainOwnerForm">
            <h1 class="googleFont">5. 반려견의 이름을 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input
                    id="input-2"
                    v-model="dog_name"
                    required
                    placeholder="Enter your dog's name."
                    ></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 6. dog_sex -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==6" class="mainOwnerForm">
            <h1 class="googleFont">6. 성별을 선택하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-select v-model="dog_sex" :options="options"></b-form-select>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 7. dog_type -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==7" class="mainOwnerForm">
            <h1 class="googleFont">7. 견종을 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input
                    id="input-2"
                    v-model="dog_type"
                    required
                    placeholder="Enter your dog type."
                    ></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 8. dog_age -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==8" class="mainOwnerForm">
            <h1 class="googleFont">8. 반려견의 나이를 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input id="age-1" v-model.number="dog_age" required type="number" placeholder="Enter your dog age."></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 9. dog_feature -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==9" class="mainOwnerForm">
            <h1 class="googleFont">9. 반려견의 특징을 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input
                    id="input-2"
                    v-model="dog_feature"
                    required
                    placeholder="Enter your dog feature."
                    ></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 10. image -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==10" class="mainOwnerForm">
            <h1 class="googleFont">10. 사진을 입력하세요.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input
                    id="input-2"
                    v-model="image"
                    required
                    placeholder="Enter your dog's image."
                    ></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">다음</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
        <!-- 11. remark -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
        <div v-if="page_num==11" class="mainOwnerForm">
            <h1 class="googleFont">11. "비고 입력란"입니다.</h1>
            <b-form>
                <b-form-group id="input-group-2">
                    <b-form-input
                    id="input-2"
                    v-model="remark"
                    required
                    placeholder="Enter remark."
                    ></b-form-input>
                </b-form-group>
                <b-button v-on:click="toPrev">이전</b-button>
                <b-button v-on:click="emptyHandler">제출</b-button>
            </b-form>
            <transition name="alertMessage" enter-active-class="animated tada" leave-active-class="animated tada">
            <h3 v-if="empty_check==1" class="googleFont">" 정보를 입력해주세요 ! "</h3>
            </transition>
        </div>
        </transition>
    </div>
</v-flex>
</template>

<script>
import 'url-search-params-polyfill';
export default {
    data() {
        return {
            img1: require('../assets/formBackgroundImg.jpg'),
            page_num: 1,
            empty_check: 0,
            user_key: '',
            uesr_nickname: '',
            lat: 0,
            lng: 0,
            title: '',
            phone_num: '',
            posted_time: '',
            posted_due: '',
            image: '',
            lost_time: '',
            date: '',
            time: '',
            dog_feature: '',
            dog_type: '',
            dog_sex: null,
            options: [
                { value: null, text: '성별을 선택하세요' },
                { value: '1', text: '암컷' },
                { value: '2', text: '수컷' }
            ],
            dog_age: 0,
            dog_name: '',
            remark: ''
        }
    },
    created() {
        let urlParams = new URLSearchParams(window.location.search);
        this.user_key = urlParams.get('user_key');
        this.user_nickname = urlParams.get('user_nickname');
        this.lat = urlParams.get('lat');
        this.lng = urlParams.get('lng');
    },
    methods: {
       onSubmit(){
           this.$store.state.user_key               = this.user_key;
           this.$store.state.user_nickname          = this.user_nickname;
           this.$store.state.ownerPost.lat          = this.lat;
           this.$store.state.ownerPost.lng          = this.lng;
           this.$store.state.ownerPost.title        = this.title;
           this.$store.state.ownerPost.phone_num    = this.phone_num;
           this.$store.state.ownerPost.posted_time  = this.posted_time;
           this.$store.state.ownerPost.posted_due   = this.posted_due;
           this.$store.state.ownerPost.image        = this.image;
           this.$store.state.ownerPost.lost_time    = this.date + ' ' + this.time;
           this.$store.state.ownerPost.dog_feature  = this.dog_feature;
           this.$store.state.ownerPost.dog_type     = this.dog_type;
           this.$store.state.ownerPost.dog_sex      = this.dog_sex;
           this.$store.state.ownerPost.dog_age      = this.dog_age;
           this.$store.state.ownerPost.dog_name     = this.dog_name;
           this.$store.state.ownerPost.remark       = this.remark;
           console.log(this.$store.state.ownerPost);
           this.$http.post('http://202.30.31.91:8000/api/ownerPosts/create',{
               title          : this.$store.state.ownerPost.title,
               phone_num      : this.$store.state.ownerPost.phone_num,
               lat            : this.$store.state.ownerPost.lat,
               lng            : this.$store.state.ownerPost.lng,
               posted_time    : this.$store.state.ownerPost.posted_time,
               posted_due     : this.$store.state.ownerPost.posted_due,
               image          : this.$store.state.ownerPost.image,
               lost_time      : this.$store.state.ownerPost.lost_time,
               dog_feature    : this.$store.state.ownerPost.dog_feature,
               dog_type       : this.$store.state.ownerPost.dog_type,
               dog_sex        : this.$store.state.ownerPost.dog_sex,
               dog_age        : this.$store.state.ownerPost.dog_age,
               dog_name       : this.$store.state.ownerPost.dog_name,
               remark         : this.$store.state.ownerPost.remark,
               user_nickname  : this.$store.state.user_nickname
           }).then(res => {
               console.log(res.data)
               this.posts = res.data
           })
        },
        toPrev(){
            this.page_num--;
            this.empty_check = 0;
        },
        emptyHandler(){
            switch(this.page_num){
                case 1: // title
                    if(this.title==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 2: // phone_num
                    if(this.phone_num==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 3: // lost_time
                    if(this.date=='' || this.time==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 4: // posted_due
                    if(this.posted_due==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 5: // dog_name
                    if(this.dog_name==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 6: // dog_sex
                    if(this.dog_sex==null){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 7: // dog_type
                    if(this.dog_type==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 8: // dog_age
                    if(this.dog_age==0){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 9: // dog_feature
                    if(this.dog_feature==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 10: // image
                    if(this.image==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 11: // remark
                    if(this.remark==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.onSubmit()
                    }
                    break;
                default:
                    alert("page num error!");
                    console.log("page num error!");
                    break;
            }
        }
    }
}
</script>


<style>
.backgroundImage {
    width: 100%;
    height: 100%;
    position: absolute;
    background-size: cover;
    background-position: center;
    top: 0;
    left: 0;
    }
    
.googleFont {
    font-family: 'Jua', sans-serif;
    color: black;
}

.mainOwnerForm {
    position: relative;
    margin-top: 110%;
    margin-left: 10%;
    margin-right: 10%;
}
</style>