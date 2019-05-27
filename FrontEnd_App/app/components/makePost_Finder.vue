<template>
    <Page class="page">
        <ActionBar title="반려견을 찾아주세요" class="action-bar" >
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_back" @tap="$goto('map')"/>
        </ActionBar>
        <GridLayout rows = "*,auto,auto,auto">
            <GridLayout row = "0">
                <ScrollView>
                    <RadDataForm ref = "dataform_f" :source = "source" :metadata="meta" :groups="groups"></RadDataForm>
                </ScrollView>
            </GridLayout>
            <Button class="btn btn-primary" row = "1" text = "위치 보기" height="50" width="100" @tap = "onTap_Loc"></Button>
            <Button class="btn btn-primary" row="2" text="사진 찍기" @tap="onTakePictureTap" horizontalAlignment="center" />
            <Button class="btn btn-primary" row = "3" @tap = "onTap_sub" text = "등록하기" :isEnabled="!processing"></Button> 
        </GridLayout>
        <!-- <ScrollView>
            <RadDataForm :source="source" :metadata="meta" :groups="groups"></RadDataForm>
        </ScrollView> -->
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
                groups: [ 
                    Object.assign(new PropertyGroup(), { 
                        name: "Finder_post",
                        collapsible: true,
                        collapsed: false 
                    }),

                ],

                meta: {
                    "commitMode": "Immediate",
                    "validationMode": "Immediate",
                    "propertyAnnotations": [{
                        "name": "title",
                        "displayName": "제목",
                        "groupName": "Finder_post",
                        "index": 0
                    }, {
                        "name": "find_time",
                        "displayName": "찾은 시간",
                        "groupName": "Finder_post",
                        "index": 1,
                        "editor":"DatePicker",

                    },{
                        "name": "find_time1",
                        "displayName": "찾은 시간",
                        "groupName": "Finder_post",
                        "index": 2,
                        "editor":"TimePicker",
                    },{
                        "name": "dog_type",
                        "displayName": "견종",
                        "groupName": "Finder_post",
                        "index": 3,
                        // "valueProvider" :["말티즈", "시츄", "슈나우져"]
                    },  {
                        "name": "dog_feature",
                        "displayName": "특징",
                        "groupName": "Finder_post",
                        "index": 4,
                    },  {
                        "name": "phone_num",
                        "displayName": "연락처",
                        "groupName": "Finder_Post",
                        "index": 5,
                    }, {
                        "name": "lat",
                        "displayName": "위도",
                        "groupName": "Finder_Post",
                        "index": 6,
                    },{
                        "name": "lng",
                        "displayName": "경도",
                        "groupName": "Finder_Post",
                        "index": 7,
                    },{
                        "name": "posted_time",
                        "displayName": "게시 시간",
                        "groupName": "Finder_Post",
                        "index": 8,
                        "editor":"DatePicker"
                    },{
                        "name": "posted_due",
                        "displayName": "게시 기간",
                        "groupName": "Finder_Post",
                        "index": 9,
                        "editor":"DatePicker",
                    },{
                        "name": "shelter_name",
                        "displayName": "유기견보호소",
                        "groupName": "Finder_Post",
                        "index": 10,
                        'editor': 'Picker',
                        'valuesProvider': [
                            "대전광역시 동물보호센터",
                            "반송원",
                            "용인시 동물보호센터",
                            "아산천사원유기견보호소",
                            "영암 유기견보호소",
                            "반려동물과함께하는내사랑바둑이",
                            "남양동물보호센터",
                            "나나우리봉사단",
                            "대관령동물병원",
                            "대장마을협동조합 반려동물놀이터"
                        ]

                    } ]
                },

                source: 
                    {
                        title : this.$store.state.FinderPost.title,
                        find_time : this.$store.state.FinderPost.find_time,
                        find_time1 : this.$store.state.FinderPost.find_time1,
                        dog_type :this.$store.state.FinderPost.dog_type,
                        dog_feature:this.$store.state.FinderPost.dog_feature,
                        phone_num:this.$store.state.FinderPost.phone_num,
                        lat: this.$store.state.FinderPost.lat,
                        lng: this.$store.state.FinderPost.lng,
                        posted_time:this.$store.state.FinderPost.posted_time,
                        posted_due:this.$store.state.FinderPost.posted_due,
                        shelter_name : this.$store.state.FinderPost.shelter_name
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
                this.$store.state.FinderPost.title = this.$refs.dataform_f.getPropertyByName('title').valueCandidate;
                this.$store.state.FinderPost.phone_num = this.$refs.dataform_f.getPropertyByName('phone_num').valueCandidate;
                this.$store.state.FinderPost.find_time = this.$refs.dataform_f.getPropertyByName('find_time').valueCandidate+" " +this.$refs.dataform_f.getPropertyByName('find_time1').valueCandidate,
                this.$store.state.FinderPost.dog_type = this.$refs.dataform_f.getPropertyByName('dog_type').valueCandidate;
                this.$store.state.FinderPost.dog_feature = this.$refs.dataform_f.getPropertyByName('dog_feature').valueCandidate;
                this.$store.state.FinderPost.posted_time = this.$refs.dataform_f.getPropertyByName('posted_time').valueCandidate;
                this.$store.state.FinderPost.posted_due = this.$refs.dataform_f.getPropertyByName('posted_due').valueCandidate;
                this.$store.state.FinderPost.shelter_name = this.$refs.dataform_f.getPropertyByName('shelter_name').valueCandidate;
                this.$goto('camera');
            },
            onTap_Loc(args){
                this.$store.state.FinderPost.title = this.$refs.dataform_f.getPropertyByName('title').valueCandidate;
                this.$store.state.FinderPost.phone_num = this.$refs.dataform_f.getPropertyByName('phone_num').valueCandidate;
                this.$store.state.FinderPost.find_time = this.$refs.dataform_f.getPropertyByName('find_time').valueCandidate+" " +this.$refs.dataform_f.getPropertyByName('find_time1').valueCandidate,
                this.$store.state.FinderPost.dog_type = this.$refs.dataform_f.getPropertyByName('dog_type').valueCandidate;
                this.$store.state.FinderPost.dog_feature = this.$refs.dataform_f.getPropertyByName('dog_feature').valueCandidate;
                this.$store.state.FinderPost.posted_time = this.$refs.dataform_f.getPropertyByName('posted_time').valueCandidate;
                this.$store.state.FinderPost.posted_due = this.$refs.dataform_f.getPropertyByName('posted_due').valueCandidate;
                this.$store.state.FinderPost.shelter_name = this.$refs.dataform_f.getPropertyByName('shelter_name').valueCandidate;
                this.$store.state.CurrentPostType = false;
                this.$goto('select_Loc');
            },
            onTap_sub(args){
                this.processing = true;
                this.$store.state.FinderPost.title = this.$refs.dataform_f.getPropertyByName('title').valueCandidate;
                this.$store.state.FinderPost.phone_num = this.$refs.dataform_f.getPropertyByName('phone_num').valueCandidate;
                this.$store.state.FinderPost.find_time = this.$refs.dataform_f.getPropertyByName('find_time').valueCandidate+" " +this.$refs.dataform_f.getPropertyByName('find_time1').valueCandidate,
                this.$store.state.FinderPost.dog_type = this.$refs.dataform_f.getPropertyByName('dog_type').valueCandidate;
                this.$store.state.FinderPost.dog_feature = this.$refs.dataform_f.getPropertyByName('dog_feature').valueCandidate;
                this.$store.state.FinderPost.posted_time = this.$refs.dataform_f.getPropertyByName('posted_time').valueCandidate;
                this.$store.state.FinderPost.posted_due = this.$refs.dataform_f.getPropertyByName('posted_due').valueCandidate;
                this.$store.state.FinderPost.shelter_name = this.$refs.dataform_f.getPropertyByName('shelter_name').valueCandidate;
                axios.post('http://210.107.198.174:8000/api/finderPosts/create',{
                    title : this.$store.state.FinderPost.title,
                    find_time : this.$store.state.FinderPost.find_time,
                    dog_type :this.$store.state.FinderPost.dog_type,
                    dog_feature:this.$store.state.FinderPost.dog_feature,
                    phone_num:this.$store.state.FinderPost.phone_num,
                    lat: this.$store.state.FinderPost.lat,
                    lng: this.$store.state.FinderPost.lng,
                    posted_time:this.$store.state.FinderPost.posted_time,
                    posted_due:this.$store.state.FinderPost.posted_due,
                    image : this.$store.state.FinderPost.image,
                    shelter_name : this.$store.state.FinderPost.shelter_name
                })
                .then(res => {
                    console.log(res.data);
                                        alert({
  title: "게시글이 등록 되었습니다.",
  message: "감사합니다!",
  okButtonText: "네!"
}).then(() => {
    this.$goto("map")
  console.log("Alert dialog closed");
});
                    //this.$goto('board');
                    })
                .catch(error => {
                    this.processing = false
                    console.log(error)});
                //console.log(this.makerinfo)
                //console.log(this.$refs.dataform.getPropertyByName('dog_age').valueCandidate);   
            }
        }
    };
</script>

<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
    ActionBar {
        background-color: #4ba5fa;
        color: #ffffff;
    }
</style>