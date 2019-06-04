<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">1. 제목을 입력하세요.</h1>
        <b-form @submit="onClick">
            <b-form-group id="input-group-2">
                <b-form-input
                id="input-2"
                v-model="title"
                required
                placeholder="Enter your title."
                ></b-form-input>
            </b-form-group>
            <b-button type="submit">다음</b-button>
        </b-form>
    </div>
</v-flex>
</template>

<script>
import 'url-search-params-polyfill';
export default {
    data() {
        return {
            img1: require('../assets/formBackgroundImg.jpg'),
            user_key : '',
            uesr_nickname : '',
            lat : 0,
            lng : 0,
            title : ''
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
       onClick(evt){
           evt.preventDefault()
           this.$store.state.FinderPost.title   =   this.title;
           this.$store.state.FinderPost.lat     =   this.lat;
           this.$store.state.FinderPost.lng     =   this.lng;
           this.$store.state.user_nickname      =   this.user_nickname;
           this.$store.state.user_key           =   this.user_key;
           console.log(this.$store.state);
           this.toNext()
        },
        toNext() {
            this.$router.push("/finderForm2");
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
</style>