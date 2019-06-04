<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">7. 유기견 보호소를 선택하세요.</h1>
        <b-form @submit="onSubmit" @reset="onClickPrev">
            <b-form-group id="input-group-2">
                <b-form-input
                id="input-2"
                v-model="shelter_name"
                required
                placeholder="Enter finding time."
                ></b-form-input>
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
            shelter_name : ''
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