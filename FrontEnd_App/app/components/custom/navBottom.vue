<template>
    <GridLayout class="navBottom" height="50" width="100%" row="3" rows="auto"
        columns="auto,auto,auto,auto">

        <GridLayout :class="selectedTab==0?'active':''" @tap="home" rows="*,auto"
            cols="auto" class="nav" col="0" row="0" width="25%">
            // <Image :class="selectedTab==0?'active':''" row="0" class="navIcon"
            //     :src="selectedTab==0?'~/assets/images/navhomem.png':'~/assets/images/navhome.png'" />
            <Label row="1" v-show="selectedTab==0" text="Home" class="navText"></Label>
        </GridLayout>
        <GridLayout :class="selectedTab==1?'active':''" @tap="cart" rows="*,auto"
            cols="auto" class="nav" col="1" row="0" width="25%">
            // <Image :class="selectedTab==1?'active':''" row="0" class="navIcon"
            //     :src="selectedTab==1?'~/assets/images/navcartm.png':'~/assets/images/navcart.png'" />
            <Label row="1" v-show="selectedTab == 1" text="Cart" class="navText"></Label>
        </GridLayout>
        <GridLayout :class="selectedTab==2?'active':''" @tap="history" rows="*,auto"
            cols="auto" class="nav" col="2" row="0" width="25%">
            // <Image :class="selectedTab==2?'active':''" row="0" class="navIcon"
            //     :src="selectedTab==2?'~/assets/images/navordersm.png':'~/assets/images/navorders.png'" />
            <Label row="1" v-show="selectedTab == 2" text="History" class="navText"></Label>
        </GridLayout>

        <GridLayout :class="selectedTab==3?'active':''" @tap="about" rows="*,auto"
            cols="auto" class="nav" col="3" row="0" width="25%">

            // <Image :class="selectedTab==3?'active':''" row="0" class="navIcon"
            //     :src="selectedTab==3?'~/assets/images/navusm.png':'~/assets/images/navus.png'" />
            <Label row="1" v-show="selectedTab == 3" text="About" class="navText"></Label>
        </GridLayout>


    </GridLayout>
</template>
<script>
    export default {
        data() {
            return {
                selectedTab: 0
            };
        },
        methods: {
            home() {
                this.selectedTab = 0;
            },
            cart() {
                this.selectedTab = 1;
            },
            history() {
                this.selectedTab = 2;
            },
            about() {
                this.selectedTab = 3;
            }
        }
    };
</script>

<style>
    .navBottom {
        background-color: #f4f4f4;
        border-color: red;
    }

    .nav {
        height: 100%;
        width: 100%;
    }

    .nav.active {
        background-color: #0Dc43776;
    }

    .navIcon {
        horizontal-align: center;
        vertical-align: center;
        height: 25
    }

    .navIcon.active {
        vertical-align: bottom;
    }

    .navText {
        margin-bottom: 2;
        font-size: 12;
        /* color: #c43776; */
        color: #d62526;
        horizontal-align: center;
    }
</style>