<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">2. 전화번호를 입력하세요.</h1>
        <b-form @submit="onClickNext" @reset="onClickPrev">
            <b-form-group id="input-group-2">
                <b-form-input
                id="input-2"
                v-model="phone_num"
                required
                placeholder="Enter your phone number."
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
            phone_num : ''
        }
    },
    methods: {
       onClickNext(evt){
           evt.preventDefault()
           this.$store.state.ownerPost.phone_num   =   this.phone_num;
           console.log(this.$store.state.ownerPost);
           this.toNext()
        },
        onClickPrev(evt){
           evt.preventDefault()
           this.$store.state.ownerPost.phone_num   =   this.phone_num;
           console.log(this.$store.state.ownerPost);
           this.toPrev()
        },
        toNext() {
            this.$router.push("/ownerForm3");
        },
        toPrev() {
            this.$router.push("/ownerForm1");
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