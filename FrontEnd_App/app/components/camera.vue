<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <Label class="action-bar-title" text="Home"></Label>
        </ActionBar>

        <GridLayout rows="auto, *, auto, auto">
            <StackLayout row="0" orientation="vertical" padding="5">
                <StackLayout orientation="horizontal" row="0" padding="5">
                    <Label text="saveToGallery" />
                    <Switch v-model="saveToGallery"/>
                </StackLayout>
                <StackLayout android:visibility="collapsed" orientation="horizontal" row="0" padding="5">
                    <Label text="allowsEditing" />
                    <Switch v-model="allowsEditing"/>
                </StackLayout>
                <StackLayout orientation="horizontal" row="0" padding="5">
                    <Label text="keepAspectRatio" />
                    <Switch v-model="keepAspectRatio"/>
                </StackLayout>
                <StackLayout orientation="horizontal" padding="5">
                    <Label text="width"></Label>
                    <TextField hint="Enter width" keyboardType="number" v-model="width" class="input"></TextField>
                    <Label text="height"></Label>
                    <TextField hint="Enter height" keyboardType="number" v-model="height" class="input"></TextField>
                </StackLayout>
            </StackLayout>
            <Image row="1" :src="cameraImage" id="image" stretch="aspectFit" margin="10"/>
            <TextView row="2" :text="labelText" editable="false"></TextView>>
            <Button row="3"  text="Take Picture" @tap="onTakePictureTap"  padding="10"/>
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
                saveToGallery: false,
                allowsEditing: false,
                keepAspectRatio: true,
                width: 320,
                height: 240,
                cameraImage: null,
                labelText: ""
            }
        },
        methods: {
            onTakePictureTap: function(args) {
                let page = (args.object).page;
                let that = this;
                requestPermissions().then(
                    () => {
                        takePicture({ width: 240, height: 240, keepAspectRatio: that.keepAspectRatio, saveToGallery: that.saveToGallery, allowsEditing: that.allowsEditing }).
                            then((imageAsset) => {
                                that.cameraImage = imageAsset;
                                fromAsset(imageAsset).then(imgSource=>{
                                    // console.log(imgSource.toBase64String('png'));
                                    // console.log(typeof(imgSource.toBase64String('png')));
                                    // console.log(imgSource.toBase64String('png').length);
                                    axios.post('http://55913c1c.ngrok.io/api/image_test',{
                                        image : imgSource.toBase64String('png'),
                                        
                                    }).then(res => {
                                        console.log("q보냄");
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