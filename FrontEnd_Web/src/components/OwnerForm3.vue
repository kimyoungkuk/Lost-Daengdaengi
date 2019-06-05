<template>
<v-flex>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
        <h1 class="googleFont">3. 잃어버린 시간을 입력하세요.</h1>
        <b-form @submit="onClickNext" @reset="onClickPrev">
            <b-form-group id="input-group-2">
                <b-form-input id="date-1" v-model="date" required type="date"></b-form-input>
                <b-form-input id="time-1" v-model="time" required type="time"></b-form-input>
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
            lost_time: '',
            date: '',
            time: ''
        }
    },
    methods: {
       onClickNext(evt){
           evt.preventDefault()
           this.lost_time = this.date + ' ' + this.time;
           this.$store.state.ownerPost.lost_time  =   this.lost_time;
           console.log(this.$store.state.ownerPost);
           this.toNext()
        },
        onClickPrev(evt){
           evt.preventDefault()
           this.lost_time = this.date + ' ' + this.time;
           this.$store.state.ownerPost.lost_time   =   this.lost_time;
           console.log(this.$store.state.ownerPost);
           this.toPrev()
        },
        toNext() {
            this.$router.push("/ownerForm4");
        },
        toPrev() {
            this.$router.push("/ownerForm2");
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