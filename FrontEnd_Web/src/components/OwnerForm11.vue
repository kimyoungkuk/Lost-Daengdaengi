<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">11. "비고 입력란"입니다.</h1>
        <b-form @submit="onSubmit" @reset="onClickPrev">
            <b-form-group id="input-group-2">
                <b-form-input
                id="input-2"
                v-model="remark"
                required
                placeholder="Enter remark."
                ></b-form-input>
            </b-form-group>
            <b-button type="reset">이전</b-button>
            <b-button type="submit">다음</b-button>
        </b-form>
    </div>
</v-flex>
</template>

<script>
export default {
    data() {
        return {
            img1: require('../assets/formBackgroundImg.jpg'),
            remark : ''
        }
    },
    methods: {
       onSubmit(evt){
           evt.preventDefault()
           this.$store.state.ownerPost.remark  =   this.remark;
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
        onClickPrev(evt){
           evt.preventDefault()
           this.$store.state.onwerPost.remark   =   this.remark;
           console.log(this.$store.state.onwerPost);
           this.toPrev()
        },
        toNext() {
            this.$router.push("/ownerForm11");
        },
        toPrev() {
            this.$router.push("/ownerForm10");
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