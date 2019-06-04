<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">7. 유기견 보호소를 선택하세요.</h1>
        <b-form @submit="onSubmit" @reset="onClickPrev">
            <b-form-group id="input-group-2">
                <b-form-select v-model="shelter_name" :options="options"></b-form-select>
            </b-form-group>
            <b-button type="reset">이전</b-button>
            <b-button type="submit">제출</b-button>
        </b-form>
    </div>
</v-flex>
</template>

<script>
export default {
    data() {
        return {
            img1: require('../assets/formBackgroundImg.jpg'),
            shelter_name : null,
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
    methods: {
       onSubmit(evt){
           evt.preventDefault()
           this.$store.state.FinderPost.shelter_name  =   this.shelter_name;
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
        },
        onClickPrev(evt){
           evt.preventDefault()
           this.$store.state.FinderPost.shelter_name   =   this.shelter_name;
           console.log(this.$store.state.FinderPost);
           this.toPrev()
        },
        toNext() {
            this.$router.push("/finderForm7");
        },
        toPrev() {
            this.$router.push("/finderForm5");
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