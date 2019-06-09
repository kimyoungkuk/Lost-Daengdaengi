<template>
    <Page class="page">
        <ActionBar title="사진과 위치를 확인합니다" class="action-bar" >
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_back" @tap="$goto('map')"/>
        </ActionBar>
        <GridLayout rows = "*,auto,auto,auto">
            <GridLayout row = "0" rows = "*,auto">
                <Image row= "0" :src="this.imageSrc" id="image" stretch="aspectFit"/>
                <ScrollView row="1" >
                    <StackLayout>
                        <RadDataForm ref = "dataform" :source = "source" :metadata="meta" :groups="groups"></RadDataForm>
                        <Label :text="this.$store.state.selected_loc" fontSize="15" horizontalAlignment="center"/>
                    </StackLayout>
                </ScrollView>
            </GridLayout>
            <Button class="btn mybtn" row = "1" text = "위치 재설정" height="50" width="100" @tap = "onTap_Loc"></Button>
            <Button class="btn mybtn" row="2" text="사진 선택" @tap="onSelectSingleTap" horizontalAlignment="center"/>
            <Button class="btn mybtn" row = "3" @tap = "onTap_sub" text = "위 정보로 게시글 작성하기"></Button> 
        </GridLayout>

    </Page>
</template>

<script>
    import { PropertyGroup } from "nativescript-ui-dataform";
    import * as geolocation from "nativescript-geolocation";
    import { Accuracy } from "tns-core-modules/ui/enums";
    import * as imagepicker from "nativescript-imagepicker";
    import { fromAsset,toBase64String } from "image-source";
    import axios from "axios";
    export default {
        data() {
            return {
                groups: [ 
                    Object.assign(new PropertyGroup(), { 
                        collapsible: true,
                        collapsed: false 
                    }),

                ],
                meta: {
                    "commitMode": "Immediate",
                    "validationMode": "Immediate",
                    "propertyAnnotations": [ {
                        "name": "lat",
                        "displayName": "위도",
                        "index": 1,
                    },{
                        "name": "lng",
                        "displayName": "경도",
                        "index": 2,
                    }]
                },
                source: 
                    {
                    },
                isSingleMode: true,
                imageAssets: [],
                imageSrc: null,
                previewSize: 300,
                thumbSize: 80,
                thumbSize: null,
                imgStr : ""
            };
        },

        methods :{
            onSelectSingleTap: function(e) {
                this.isSingleMode = true;
                let context = imagepicker.create({ mode: "single" });
                this.startSelection(context);
            },
            startSelection(context) {
                context
                    .authorize()
                    .then(() => {
                        this.imageAssets = [];
                        this.imageSrc = null;
                        return context.present();
                    })
                    .then((selection) => {
                        console.log((selection));
                        this.imageSrc = this.isSingleMode && selection.length > 0 ? selection[0] : null;
                        // set the images to be loaded from the assets with optimal sizes (optimize memory usage)
                        selection.forEach(element => {
                            element.options.width = this.isSingleMode ? this.previewSize : this.thumbSize;
                            element.options.height = this.isSingleMode ? this.previewSize : this.thumbSize;
                        });
                        this.imageAssets = selection;
                        fromAsset(selection[0]).then(imgSource=>{
                           this.imgStr = imgSource.toBase64String('png');
                        })
            
                    }).catch(function (e) {
                        console.log(e);
                    });
                    
            },
            onTap_Loc(args){
                this.$store.state.CurrentPostType = true;
                this.$goto('select_Loc');
            },
            onTap_sub(args){
                this.$store.state.ownerPost.image = this.imgStr;
                axios.post(this.$store.state.API_BACKEND_URL + '/api/ownerPosts/create/before',{
                    user_nickname : this.$store.state.user_nickname,
                    title : this.$store.state.ownerPost.title,
                    dog_name : this.$store.state.ownerPost.dog_name,
                    lost_time : this.$store.state.ownerPost.lost_time,
                    dog_sex :this.$store.state.ownerPost.dog_sex,
                    dog_type :this.$store.state.ownerPost.dog_type,
                    dog_age :this.$store.state.ownerPost.dog_age,
                    dog_feature:this.$store.state.ownerPost.dog_feature,
                    remark:this.$store.state.ownerPost.remark,
                    phone_num:this.$store.state.ownerPost.phone_num,
                    lat: this.$store.state.ownerPost.lat,
                    lng: this.$store.state.ownerPost.lng,
                    posted_time:this.$store.state.ownerPost.posted_time,
                    posted_due:this.$store.state.ownerPost.posted_due,
                    image : this.$store.state.ownerPost.image
                })
                .then(res => {
                    console.log(res.data);
                    alert({
                        title: "위 정보로 게시글을 작성합니다.",
                        message: " ",
                        okButtonText: "게시글 작성하기"
                        }).then(() => {
                        this.$goto('makeOwnerPostWeb');
                        console.log("Alert dialog closed");
                        });
                    }).catch(error => {console.log(error)});
                
            }
            
        }
    };
</script>
<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
    ActionBar {
        background-color: #FA7268;
        color: #ffffff;
    }
    .mybtn{
  color: #FA7268;
  background-color: #FFFFFF;
}
</style>