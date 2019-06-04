<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">9. 반려견의 특징을 입력하세요.</h1>
        <b-form @submit="onClickNext" @reset="onClickPrev">
            <b-form-group id="input-group-2">
                <b-form-input
                id="input-2"
                v-model="dog_feature"
                required
                placeholder="Enter your dog feature."
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
            dog_feature : ''
        }
    },
    methods: {
       onClickNext(evt){
           evt.preventDefault()
           this.$store.state.ownerPost.dog_feature   =   this.dog_feature;
           console.log(this.$store.state.ownerPost);
           this.toNext()
        },
        onClickPrev(evt){
           evt.preventDefault()
           this.$store.state.ownerPost.dog_feature   =   this.dog_feature;
           console.log(this.$store.state.ownerPost);
           this.toPrev()
        },
        toNext() {
            this.$router.push("/ownerForm10");
        },
        toPrev() {
            this.$router.push("/ownerForm9");
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