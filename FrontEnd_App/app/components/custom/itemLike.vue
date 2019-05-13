<template>
    <!-- <GridLayout marginTop="5" width="100%" row="3" columns="auto,*,auto,auto" rows="auto"> -->
    <GridLayout columns="auto,*,auto,auto" rows="auto">
        <GridLayout col="0" rows="auto" columns="auto,auto" @tap="toggleLike">
            <Label col="0" row="0" ref="like" class="like-icon fa" :class="[item.isLike ? 'liked-active' : 'default']"
                :text="item.isLike ? 'fa-thumbs-up':'fa-thumbs-o-up' | fonticon" />
            <Label col="1" row="0" class="layout" :text="item.likes"></Label>
        </GridLayout>
        <StackLayout col="1" orientation="horizontal" marginLeft="15">
            <Label ref="" class="like-icon layout fa" :text="'fa-comment-o' | fonticon" />
            <Label class="layout" :text="item.comments"></Label>
        </StackLayout>
        <GridLayout col="2" rows="auto" columns="auto,auto" @tap="toggleHeart"
            marginRight="15">
            <Label col="0" row="0" ref="관심" class="like-icon  fa"
                :class="[item.isFavorite ? 'heart-active' : 'default']" :text="item.isFavorite ? 'fa-heart':'fa-heart-o' | fonticon" />
            <Label col="1" row="0" class="layout" text="관심"></Label>
        </GridLayout>
        <StackLayout col="3" orientation="horizontal">
            <Label ref="" class="like-icon layout fa" :text="'fa-share-square-o' | fonticon" />
            <Label class="layout" text="공유"></Label>
        </StackLayout>

    </GridLayout>
</template>

<script>
    import {
        isIOS,
        isAndroid
    } from "tns-core-modules/platform";
    export default {
        props: ["item"],
        components: {},
        computed: {
            categoryIcon() {
                switch (this.item.category) {
                    case "Burger":
                        return "fa-cutlery";
                        break;
                    case "Beer":
                        return "fa-beer";
                        break;
                    case "Pancake":
                        return "fa-coffee";
                        break;
                    case "Cake":
                        return "fa-birthday-cake";
                        break;
                    default:
                        return "fa-fire";
                        break;
                }
            }
        },
        created() {
            // this.isLike =  this.item.isLike
            // this.isHeart =  this.item.isFavorite
        },
        mounted() {},
        methods: {
            animateLike() {
                if (isIOS) {
                    return;
                }
                let imgLogo = this.$refs.like.nativeView;
                imgLogo
                    .animate({
                        scale: {
                            x: 0.6,
                            y: 0.6
                        },
                        duration: 100,
                        delay: 0
                    })
                    .then(function() {
                        return imgLogo.animate({
                            scale: {
                                x: 1.2,
                                y: 1.2,
                                duration: 50
                            }
                        });
                    })
                    .then(function() {
                        return imgLogo.animate({
                            scale: {
                                x: 1,
                                y: 1,
                                duration: 100
                            }
                        });
                    })
                    .then(function() {});
            },
            animateFavorite() {
                if (isIOS) {
                    return;
                }
                let imgLogo = this.$refs.favorite.nativeView;
                imgLogo
                    .animate({
                        scale: {
                            x: 0.6,
                            y: 0.6
                        },
                        duration: 50,
                        delay: 0
                    })
                    .then(function() {
                        return imgLogo.animate({
                            scale: {
                                x: 1.2,
                                y: 1.2,
                                duration: 50
                            }
                        });
                    })
                    .then(function() {
                        return imgLogo.animate({
                            scale: {
                                x: 1,
                                y: 1,
                                duration: 100
                            }
                        });
                    })
                    .then(function() {});
            },
            toggleLike() {
                this.animateLike();
                this.item.isLike = !this.item.isLike;
                if (this.item.isLike) {
                    this.item.likes += 1;
                } else {
                    this.item.likes -= 1;
                }
            },
            toggleHeart() {
                this.animateFavorite();
                this.item.isFavorite = !this.item.isFavorite;
            },
            onClickButton() {
                this.$emit("clicked", this.item);
            }
        },
        data() {
            return {
                isLike: false,
                isHeart: false
            };
        }
    };
</script>
<style scoped>
    .item-category {
        font-size: 14;
        color: #828282;
    }

    .rating-icon {
        padding-top: 3;
        color: #FFE900;
        font-size: 14;
        margin-left: 10;
    }

    .rating-value {
        margin-left: 5;
    }

    .liked-active {
        color: #4080FF;
    }

    .heart-active {
        color: #b51213;
    }

    .default {
        color: #828282;
    }

    .layout {
        vertical-align: bottom;
        color: #828282;
        font-size: 14;
        height: 30;
        padding: 5 0 5 0;
    }

    .like-icon {
        vertical-align: bottom;
        height: 30;
        font-size: 16;
        margin-right: 2;
        padding: 5 5 5 5;
    }

    .item-name {
        font-size: 14;
        font-weight: bold;
    }

    .item-category {
        font-size: 14;
        color: #828282;
    }

    .category-icon {
        text-align: center;
        padding-top: 5;
        border-color: white;
        color: white;
        vertical-align: center;
        font-size: 25;
        border-width: 1;
        border-radius: 50%;
        margin-top: 4;
        margin-right: 15;
        width: 40;
        height: 40;
    }

    .content {
        margin-left: 16;
        margin-right: 16;
        margin-bottom: 3;
        margin-top: 16;
    }

    .card-img {
        width: 100%;
        height: 150;
        margin-bottom: 10;
    }

    .line {
        height: 0.5;
        border: none;
        color: #e0e0e0;
        background-color: #e0e0e0;
    }

    .lineBreak {
        height: 7;
        border: none;
        color: #e0e0e0;
        background-color: #e0e0e0;
    }
</style>