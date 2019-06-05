<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">        
        <!-- 1. title-->
        <transition appear name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
            <div v-if="page_num==1" class="mainForm">
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
                <h3 v-if="empty_check==1" class="googleFont"> 정보를 입력해주세요 ! "</h3>
                </transition>
            </div>
        </transition>
        <!-- 2. phone_num -->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
            <div v-if="page_num==2" class="mainForm">
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
        <!-- 3. find_time-->
        <transition name="router-anim" mode="out-in" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
            <div v-if="page_num==3" class="mainForm">
                <h1 class="googleFont">3. 발견 시간을 입력하세요.</h1>
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
        <!-- 4. posted_due-->
        <transition name="router-anim" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
            <div v-if="page_num==4" class="mainForm">
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
        <!-- 5. dog_feature-->
        <transition name="router-anim" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
            <div v-if="page_num==5" class="mainForm">
                <h1 class="googleFont">5. 특징을 입력하세요.</h1>
                <b-form>
                    <b-form-group id="input-group-2">
                        <b-form-input
                        id="input-2"
                        v-model="dog_feature"
                        required
                        placeholder="Enter dog's feature."
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
        <!-- 6. image -->
        <transition name="router-anim" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
            <div v-if="page_num==6" class="mainForm">
                <h1 class="googleFont">6. 사진을 입력하세요.</h1>
                <b-form>
                    <b-form-group id="input-group-2">
                        <b-form-input
                        id="input-2"
                        v-model="image"
                        required
                        placeholder="Enter finding time."
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
        <!-- 7. shelter_name -->
        <transition name="router-anim" enter-active-class="animated rollIn" leave-active-class="animated rollOut">
            <div v-if="page_num==7" class="mainForm">
                <h1 class="googleFont">7. 유기견 보호소를 선택하세요.</h1>
                <b-form @submit="onSubmit">
                    <b-form-group id="input-group-2">
                        <b-form-select v-model="shelter_name" :options="options"></b-form-select>
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
            user_nickname: '',
            lat: 0,
            lng: 0,
            title: '',
            phone_num: '',
            find_time: '',
            date: '',
            time: '',
            posted_due: '',
            dog_feature: '',
            image: '',
            shelter_name: null,
            options: [
                { value: null, text: '유기견 보호소를 선택해 주세요' },
                { value: '대전광역시 동물보호센터', text: '대전광역시 동물보호센터' },
                { value: '반송원', text: '반송원' },
                { value: '용인시 동물보호센터', text: '용인시 동물보호센터' },
                { value: '아산천사원유기견보호소', text: '아산천사원유기견보호소'},
                { value: '영암 유기견보호소', text: '영암 유기견보호소' },
                { value: '반려동물과함께하는내사랑바둑이', text: '반려동물과함께하는내사랑바둑이' },
                { value: '남양동물보호센터', text: '남양동물보호센터' },
                { value: '나나우리봉사단', text: '나나우리봉사단' },
                { value: '대관령동물병원', text: '대관령동물병원' },
                { value: '대장마을협동조합 반려동물놀이터', text: '대장마을협동조합 반려동물놀이터' }
            ]
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
            this.$store.state.user_key                   = this.user_key;
            this.$store.state.user_nickname              = this.user_nickname;
            this.$store.state.FinderPost.lat             = this.lat;
            this.$store.state.FinderPost.lng             = this.lng;
            this.$store.state.FinderPost.title           = this.title;
            this.$store.state.FinderPost.phone_num       = this.phone_num;
            this.$store.state.FinderPost.find_time       = this.date + ' ' + this.time;
            this.$store.state.FinderPost.posted_due      = this.posted_due;
            this.$store.state.FinderPost.dog_feature     = this.dog_feature;
            this.$store.state.FinderPost.image           = this.image;
            this.$store.state.FinderPost.shelter_name    = this.shelter_name;
            console.log(this.$store.state.FinderPost);
            this.$http.post('http://202.30.31.91:8000/api/finderPosts/create',{
                title          : this.$store.state.FinderPost.title,
                phone_num      : this.$store.state.FinderPost.phone_num,
                lat            : this.$store.state.FinderPost.lat,
                lng            : this.$store.state.FinderPost.lng,
                posted_time    : this.$store.state.FinderPost.posted_time,
                posted_due     : this.$store.state.FinderPost.posted_due,
                image          : this.$store.state.FinderPost.image,
                find_time      : this.$store.state.FinderPost.find_time,
                dog_feature    : this.$store.state.FinderPost.dog_feature,
                dog_type       : this.$store.state.FinderPost.dog_type,
                shelter_name   : this.$store.state.FinderPost.shelter_name,
                user_nickname  : this.$store.state.user_nickname
            }).then(res => {
                console.log(res.data)
                this.posts = res.data
            })
            this.toReload()
        },
        toPrev(){
            this.page_num--;
            this.empty_check = 0;
        },
        toReload(){
            this.$router.push("/ownerBoard");
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
                case 3: // find_time
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
                case 5: // dog_feature
                    if(this.dog_feature==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 6: // image
                    if(this.image==''){
                        this.empty_check = 1;
                    }
                    else{
                        this.page_num++;
                        this.empty_check = 0;
                    }
                    break;
                case 7: // shelter_name
                    if(this.shelter_name==null){
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
    color:cornsilk;
}

/* .mainForm {
    position: relative;
    left: 300px;
    top: 50px;
} */

/* .fixed-pos transition{
    position: absolute;
} */
</style>