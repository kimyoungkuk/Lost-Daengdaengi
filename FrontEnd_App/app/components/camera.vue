<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <Label class="action-bar-title" text="카메라"></Label>
        </ActionBar>

        <GridLayout rows=" *, auto, auto,auto">
            
            <Image row="0" :src="cameraImage" id="image" stretch="aspectFit" margin="10"/>
            <TextView row="1" :text="labelText" editable="false"></TextView>>
            <Button class="btn btn-primary" row="2"  text="사진찍기" @tap="onTakePictureTap"  padding="10"/>
            <Button class="btn btn-primary" row ="3" text = "맞습니다" @tap="onSelect" paddin="10"/>
        </GridLayout>
    </Page>
</template>

<script>
    import { EventData, Observable, fromObject } from "tns-core-modules/data/observable";
    import { Page } from "tns-core-modules/ui/page";
    import { View } from 'tns-core-modules/ui/core/view';
    import { takePicture, requestPermissions } from "nativescript-camera";
    import { fromAsset,toBase64String } from "image-source";
    import axios from "axios";
    export default {
        data() {
            return {
                imgStr : "",
                saveToGallery: false,
                allowsEditing: false,
                keepAspectRatio: true,
                width: 160,
                height: 120,
                cameraImage: null,
                labelText: ""
            }
        },
        methods: {
            onSelect(args){
                this.$store.state.FinderPost.dog_type = this.labelText;
                this.$goto('makePost_Finder');
            },
            onTakePictureTap: function(args) {
                let page = (args.object).page;
                let that = this;
                requestPermissions().then(
                    () => {
                        takePicture({ width: 160, height: 120, keepAspectRatio: that.keepAspectRatio, saveToGallery: that.saveToGallery, allowsEditing: that.allowsEditing }).
                            then((imageAsset) => {
                                that.cameraImage = imageAsset;
                                fromAsset(imageAsset).then(imgSource=>{
                                    this.$store.state.FinderPost.image = imgSource.toBase64String('png');
                                    // console.log(imgSource.toBase64String('png'));
                                    // console.log(typeof(imgSource.toBase64String('png')));
                                    // console.log(imgSource.toBase64String('png').length);
                                    //
                                    axios.post('http://202.30.31.91:8000/api/classification',{
                                        image : imgSource.toBase64String('png'),
                                        
                                    }).then(res => {
                                        console.log("q보냄");
                                        console.log(res.data);
                                        this.labelText = res.data;
                                        
                                    }).catch(err=>{})
                                })
                                
                            },
                            (err) => {
                                console.log("Error -> " + err.message);
                            });
                    },
                    () => alert('permissions rejected')
                );
            }
        }
    };
</script>

<style scoped lang="scss">
@import '~nativescript-theme-core/css/core.light.css';
    ActionBar {
        background-color: #4ba5fa;
        color: #ffffff;
    }
    // // Start custom common variables
    // @import '../app-variables';
    // // End custom common variables
    // // Custom styles
    // .fa {
    //     color: $accent-dark;
    // }
    // .info {
    //     font-size: 20;
    // }
</style>