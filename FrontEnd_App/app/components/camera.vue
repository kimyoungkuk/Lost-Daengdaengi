<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <Label class="action-bar-title" text="댕댕이 사진을 지정 합니다"></Label>
        </ActionBar>
        <GridLayout rows=" *, auto, auto,auto,auto">
            <Image row="0" :src="cameraImage" id="image" stretch="aspectFit"/>
            <TextView row="1" :text="labelText" editable="false"></TextView>>
            <Progress color="#FA7268" v-show="loadingComplete" :value="loadingValue" row ="2"/>
            <Button class="btn mybtn" row="3"  text="댕댕이 촬영" @tap="onTakePictureTap" padding="10"/>
            <Button class="btn mybtn" row ="4" text = "추천된 견종을 사용합니다." :isEnabled="!processing" @tap="onSelect" padding="10"/>
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
                processing: true,
                loadingValue: 0,
                loadingComplete: false,
                imgStr : "",
                saveToGallery: false,
                allowsEditing: false,
                keepAspectRatio: false,
<<<<<<< HEAD
                width: 224,
                height: 224,
                cameraImage: null,
                labelText: ""
=======
                width: 160,
                height: 120,
                cameraImage: '~/assets/images/DaengDaengi.png',
                labelText: "-"
>>>>>>> 3b45ef09c508fb106b23b971250aa27cde8d4dca
            }
        },
        methods: {
            OnInit() {
                this.labelText = "-"
                this.loadingValue = 0;
    var d = setInterval(() => {
      this.loadingValue += 1
      if(this.loadingValue==90){
        clearInterval(d)
      }
    }, 60)
  },
            onSelect(args){
                this.$store.state.FinderPost.dog_type = this.labelText;
                this.$goto('makePost_Finder');
            },
            onTakePictureTap: function(args) {
                let page = (args.object).page;
                let that = this;
                requestPermissions().then(
                    () => {
                        takePicture({ width: 224, height: 224, keepAspectRatio: that.keepAspectRatio, saveToGallery: that.saveToGallery, allowsEditing: that.allowsEditing }).
                            then((imageAsset) => {
                                that.cameraImage = imageAsset;
                                fromAsset(imageAsset).then(imgSource=>{
<<<<<<< HEAD
                                    this.$store.state.FinderPost.image = imgSource.toBase64String('jpeg');
=======
                                    this.$store.state.FinderPost.image = imgSource.toBase64String('jpg');
>>>>>>> 3b45ef09c508fb106b23b971250aa27cde8d4dca
                                    // console.log(imgSource.toBase64String('png'));
                                    // console.log(typeof(imgSource.toBase64String('png')));
                                    // console.log(imgSource.toBase64String('png').length);
                                    //
                                    this.loadingComplete= true
                                    this.OnInit()
                                    axios.post('http://202.30.31.91:8000/api/classification',{
<<<<<<< HEAD
                                        image : imgSource.toBase64String('jpeg'),
                                        
=======
                                        image : imgSource.toBase64String('jpg'),
>>>>>>> 3b45ef09c508fb106b23b971250aa27cde8d4dca
                                    }).then(res => {
                                        console.log("보냄");
                                        this.loadingComplete=false
                                        this.processing = false
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
        background-color: #FA7268;
        color: #ffffff;
    }
          .mybtn{
      color: #ffffff;
      background-color: #FA7268;
    }
</style>