<template>
    <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
        <v-flex>
            <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">  
            <div class="googleFont_finder">
                    <div class="submitTitle">
                        <transition appear name="slide-up">
                            <div><h1>Lost-Daengdaengi</h1></div>
                        </transition>
                        <transition appear name="slide-left">
                            <div><h1>제출 완료</h1></div>
                        </transition>
                        <transition appear name="slide-right">
                            <div><h1>이용해주셔서 감사합니다.</h1></div>
                        </transition>
                        <transition appear name="slide-down">
                            <div><h1>*^ㅡ^*</h1></div>
                        </transition>
                    </div>
                </div>
                <transition
                :duration="100000"
                appear
                name="custom-classes-transition"
                enter-active-class="animated shake">
                    <div id="submitSpace">
                        <b-form>
                            <b-button class="btn btn-primary custom-btn" v-on:click="goOut">닫기</b-button>
                        </b-form>
                    </div>
                </transition>
        </v-flex>
    </div>
</template>

<script>
export default {
    data() {
        return {
            img1: require('../assets/submitImg.jpg')
        }
    },
    methods: {
        goOut(){
            location.replace('http://202.30.31.91/SubmitPage?action=done');
        }
    }
}
</script>

<style>
.submitTitle {
    margin-top: 20%;
}

#submitSpace {
    margin-top: 5%;
}


.slide-up {
    transition: all 0.25s;
}
.slide-up-enter-active {
    transition: all 0.25s ease;
    transition-duration: 5s;
}
.slide-up-leave-active { 
    transition: all 0.25s cubic-bezier(0.075, 0.82, 0.165, 1);
}
.slide-up-enter, .slide-up-leave-active { 
    opacity: 0; transform: translateY(-100%);
}



.slide-down {
    transition: all 0.25s;
}
.slide-down-enter-active {
    transition: all 0.25s ease;
    transition-duration: 5s;
}
.slide-down-leave-active { 
    transition: all 0.25s cubic-bezier(1, 0.5, 0.8, 1); 
}
.slide-down-enter, .slide-down-leave-active { 
    opacity: 0; transform: translateY(100%); 
}


.slide-right {
    transition: all 0.25s;
}
.slide-right-enter-active {
    transition: all 0.25s ease;
    transition-duration: 5s;
}
.slide-right-leave-active { 
    transition: all 0.25s cubic-bezier(1, 0.5, 0.8, 1); 
}
.slide-right-enter, .slide-right-leave-active { 
    opacity: 0; transform: translateX(100%); 
}

.slide-left {
    transition: all 0.25s;
}
.slide-left-enter-active {
    transition: all 0.25s ease;
    transition-duration: 5s;
}
.slide-left-leave-active { 
    transition: all 0.25s cubic-bezier(1, 0.5, 0.8, 1); 
}
.slide-left-enter, .slide-left-leave-active { 
    opacity: 0; transform: translateX(-100%); 
}
</style>