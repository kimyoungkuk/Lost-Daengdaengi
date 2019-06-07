<template>
    <Page class="page">
        <ActionBar title="견종과 위치를 확인합니다" class="action-bar" >
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_back" @tap="$goto('map')"/>
        </ActionBar>
        <GridLayout rows = "*,auto,auto,auto">
            <GridLayout row = "0" rows = "*,auto">
                <Image row= "0" :src="this.imageAsset" id="image" stretch="aspectFit"/>
                <ScrollView row="1" >
                    <RadDataForm ref = "dataform_f" :source = "source" :metadata="meta" :groups="groups"></RadDataForm>
                </ScrollView>
            </GridLayout>
            <Button class="btn mybtn" row = "1" text = "위치 재설정" height="50" width="100" @tap = "onTap_Loc"></Button>
            <Button class="btn mybtn" row="2" text="사진 재촬영" @tap="onTakePictureTap" horizontalAlignment="center" />
            <Button class="btn mybtn" row = "3" @tap = "onTap_sub" text = "위 정보로 게시글 작성하기" :isEnabled="!processing"></Button> 
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
                processing : false,
                imageAsset : this.$store.state.imageAsset,
                groups: [ 
                    Object.assign(new PropertyGroup(), { 
                        collapsible: true,
                        collapsed: false 
                    }),
                ],
                meta: {
                    "commitMode": "Immediate",
                    "validationMode": "Immediate",
                    "propertyAnnotations": [{
                        "name": "dog_type",
                        "displayName": "견종을 확인하고 수정해주세요",
                        "groupName": "",
                        "index": 0,
                    },  {
                        "name": "lat",
                        "displayName": "위도",
                        "groupName": "",
                        "index": 1,
                    },{
                        "name": "lng",
                        "displayName": "경도",
                        "groupName": "",
                        "index": 2,
                    }]
                },
                source: 
                    {
                        dog_type :this.$store.state.FinderPost.dog_type,
                        lat: this.$store.state.FinderPost.lat,
                        lng: this.$store.state.FinderPost.lng,
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
            onTakePictureTap(args){
                this.$store.state.FinderPost.dog_type = this.$refs.dataform_f.getPropertyByName('dog_type').valueCandidate;
                this.$goto('camera');
            },
            onTap_Loc(args){
                this.$store.state.FinderPost.dog_type = this.$refs.dataform_f.getPropertyByName('dog_type').valueCandidate;
                this.$store.state.CurrentPostType = false;
                this.$goto('select_Loc');
            },
            onTap_sub(args){
                this.processing = true;
                this.$store.state.FinderPost.dog_type = this.$refs.dataform_f.getPropertyByName('dog_type').valueCandidate;
                axios.post(this.$store.state.API_BACKEND_URL + '/api/finderPosts/create/before',{
                    user_nickname : this.$store.state.user_nickname,
                    title : this.$store.state.FinderPost.title,
                    find_time : this.$store.state.FinderPost.find_time,
                    dog_type :this.$store.state.FinderPost.dog_type,
                    dog_feature:this.$store.state.FinderPost.dog_feature,
                    phone_num:this.$store.state.FinderPost.phone_num,
                    lat: this.$store.state.FinderPost.lat,
                    lng: this.$store.state.FinderPost.lng,
                    posted_due:this.$store.state.FinderPost.posted_due,
                    image : this.$store.state.FinderPost.image,
                    shelter_name : this.$store.state.FinderPost.shelter_name
                })
                .then(res => {
                    console.log(res.data);
                    alert({
                        title: "위 정보로 게시글을 작성합니다.",
                        message: " ",
                        okButtonText: "게시글 작성하기"
                        }).then(() => {
                            this.$goto("makeFinderPostWeb")
                        console.log("Alert dialog closed");
                        });
                    })
                .catch(error => {
                    this.processing = false
                    console.log(error)}); 
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