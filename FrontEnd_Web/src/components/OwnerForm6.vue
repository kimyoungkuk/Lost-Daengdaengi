<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">6. 성별을 선택하세요.</h1>
        <b-form @submit="onClickNext" @reset="onClickPrev">
            <b-form-group id="input-group-2">
                <b-form-select v-model="dog_sex" :options="options"></b-form-select>
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
            dog_sex : null,
            options: [
                { value: null, text: '성별을 선택하세요' },
                { value: '1', text: '암컷' },
                { value: '2', text: '수컷' }
            ]
        }
    },
    methods: {
       onClickNext(evt){
           evt.preventDefault()
           this.$store.state.ownerPost.dog_sex  =   this.dog_sex;
           console.log(this.$store.state.ownerPost);
           this.toNext()
        },
        onClickPrev(evt){
           evt.preventDefault()
           this.$store.state.ownerPost.dog_sex   =   this.dog_sex;
           console.log(this.$store.state.ownerPost);
           this.toPrev()
        },
        toNext() {
            this.$router.push("/ownerForm7");
        },
        toPrev() {
            this.$router.push("/ownerForm5");
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