<template>
    <Page class="page">
        <ActionBar title="Home" class="action-bar" >
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_back" @tap="$goto('map')"/>
        </ActionBar>
        <GridLayout rows = "*,auto,auto,auto">
            <GridLayout row = "0">
                <ScrollView>
                    <RadDataForm ref = "dataform" :source = "source" :metadata="meta" :groups="groups"></RadDataForm>
                </ScrollView>
            </GridLayout>
            <Button row = "1" text = "위치 보기" height="50" width="100" @tap = "onTap_Loc"></Button>
            <Button row="2" text="사진 선택" @tap="onSelectSingleTap" horizontalAlignment="center" />
            <Button row = "3" @tap = "onTap_sub" text = "등록하기"></Button>
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
                groups: [ 
                    Object.assign(new PropertyGroup(), { 
                        name: "Owner_post",
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
                        "groupName": "Owner_post",
                        "index": 1
                    },{
                        "name": "dog_name",
                        "displayName": "강아지 이름",
                        "groupName": "Owner_post",
                        "index": 2
                    }, {
                        "name": "lost_time",
                        "displayName": "잃어버린 시간",
                        "groupName": "Owner_post",
                        "index": 3,
                        "editor":"DatePicker",

                    },{
                        "name": "lost_time1",
                        "displayName": "잃어버린 시간",
                        "groupName": "Owner_post",
                        "index": 4,
                        "editor":"TimePicker",
                    }, {
                        "name": "dog_sex",
                        "displayName": "성별",
                        "groupName": "Owner_post",
                        "index": 5,
                    },{
                        "name": "dog_type",
                        "displayName": "견종",
                        "groupName": "Owner_post",
                        "index": 6,
                        // "valueProvider" :["말티즈", "시츄", "슈나우져"]
                    }, {
                        "name": "dog_age",
                        "displayName": "나이",
                        "groupName": "Owner_post",
                        "index": 7,
                        // "editor" : "Stepper"
                    }, {
                        "name": "dog_feature",
                        "displayName": "특징",
                        "groupName": "Owner_post",
                        "index": 8,
                    }, {
                        "name": "remark",
                        "displayName": "비고",
                        "groupName": "Owner_post",
                        "index": 9,
                    }, {
                        "name": "phone_num",
                        "displayName": "연락처",
                        "groupName": "Owner_Post",
                        "index": 10,
                    }, {
                        "name": "lat",
                        "displayName": "위도",
                        "groupName": "Owner_Post",
                        "index": 11,
                    },{
                        "name": "lng",
                        "displayName": "경도",
                        "groupName": "Owner_Post",
                        "index": 12,
                    },{
                        "name": "posted_time",
                        "displayName": "게시 시간",
                        "groupName": "Owner_Post",
                        "index": 13,
                        "editor":"DatePicker"
                    },{
                        "name": "posted_due",
                        "displayName": "게시 기간",
                        "groupName": "Owner_Post",
                        "index": 14,
                        "editor":"DatePicker",
                    } ]
                },

                source: 
                    {
                        title : this.$store.state.ownerPost.title,
                        dog_name : this.$store.state.ownerPost.dog_name,
                        lost_time : this.$store.state.ownerPost.lost_time,
                        lost_time1 : this.$store.state.ownerPost.lost_time1,
                        dog_sex :this.$store.state.ownerPost.dog_sex,
                        dog_type :this.$store.state.ownerPost.dog_type,
                        dog_age :this.$store.state.ownerPost.dog_age,
                        dog_feature:this.$store.state.ownerPost.dog_age,
                        remark:this.$store.state.ownerPost.remark,
                        phone_num:this.$store.state.ownerPost.phone_num,
                        lat: this.$store.state.ownerPost.lat,
                        lng: this.$store.state.ownerPost.lng,
                        posted_time:this.$store.state.ownerPost.posted_time,
                        posted_due:this.$store.state.ownerPost.posted_due,
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
                        console.log((this.imageSrc).toBase64String('png'));
            
                    }).catch(function (e) {
                        console.log(e);
                    });
                    
            },
            onTap_Loc(args){
                this.$store.state.ownerPost.title = this.$refs.dataform.getPropertyByName('title').valueCandidate;
                this.$store.state.ownerPost.phone_num = this.$refs.dataform.getPropertyByName('phone_num').valueCandidate;
                this.$store.state.ownerPost.dog_name = this.$refs.dataform.getPropertyByName('dog_name').valueCandidate;
                this.$store.state.ownerPost.lost_time = this.$refs.dataform.getPropertyByName('lost_time').valueCandidate+" " +this.$refs.dataform.getPropertyByName('lost_time1').valueCandidate,
                this.$store.state.ownerPost.dog_sex = this.$refs.dataform.getPropertyByName('dog_sex').valueCandidate;
                this.$store.state.ownerPost.dog_type = this.$refs.dataform.getPropertyByName('dog_type').valueCandidate;
                this.$store.state.ownerPost.dog_age = this.$refs.dataform.getPropertyByName('dog_age').valueCandidate;
                this.$store.state.ownerPost.dog_feature = this.$refs.dataform.getPropertyByName('dog_feature').valueCandidate;
                this.$store.state.ownerPost.remark = this.$refs.dataform.getPropertyByName('remark').valueCandidate;
                this.$store.state.ownerPost.image = this.imgStr;
                this.$store.state.ownerPost.posted_time = this.$refs.dataform.getPropertyByName('posted_time').valueCandidate;
                this.$store.state.ownerPost.posted_due = this.$refs.dataform.getPropertyByName('posted_due').valueCandidate;
                 this.$store.state.CurrentPostType = true;
                this.$goto('select_Loc');
            },
            onTap_sub(args){
                console.log(this.$refs.dataform.getPropertyByName('phone_num').valueCandidate);
                this.$store.state.ownerPost.title = this.$refs.dataform.getPropertyByName('title').valueCandidate;
                this.$store.state.ownerPost.phone_num = this.$refs.dataform.getPropertyByName('phone_num').valueCandidate;
                this.$store.state.ownerPost.dog_name = this.$refs.dataform.getPropertyByName('dog_name').valueCandidate;
                this.$store.state.ownerPost.lost_time = this.$refs.dataform.getPropertyByName('lost_time').valueCandidate+" " +this.$refs.dataform.getPropertyByName('lost_time1').valueCandidate,
                this.$store.state.ownerPost.dog_sex = this.$refs.dataform.getPropertyByName('dog_sex').valueCandidate;
                this.$store.state.ownerPost.dog_type = this.$refs.dataform.getPropertyByName('dog_type').valueCandidate;
                this.$store.state.ownerPost.dog_age = this.$refs.dataform.getPropertyByName('dog_age').valueCandidate;
                this.$store.state.ownerPost.dog_feature = this.$refs.dataform.getPropertyByName('dog_feature').valueCandidate;
                this.$store.state.ownerPost.remark = this.$refs.dataform.getPropertyByName('remark').valueCandidate;
                this.$store.state.ownerPost.image = this.imgStr;
                this.$store.state.ownerPost.posted_time = this.$refs.dataform.getPropertyByName('posted_time').valueCandidate;
                this.$store.state.ownerPost.posted_due = this.$refs.dataform.getPropertyByName('posted_due').valueCandidate;
                axios.post('http://210.107.198.174:8000/api/ownerPosts/create',{
                    title : this.$store.state.ownerPost.title,
                    dog_name : this.$store.state.ownerPost.dog_name,
                    lost_time : this.$store.state.ownerPost.lost_time,
                    lost_time1 : this.$store.state.ownerPost.lost_time1,
                    dog_sex :this.$store.state.ownerPost.dog_sex,
                    dog_type :this.$store.state.ownerPost.dog_type,
                    dog_age :this.$store.state.ownerPost.dog_age,
                    dog_feature:this.$store.state.ownerPost.dog_age,
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
  title: "게시글이 등록 되었습니다.",
  message: "곧 찾을거에요!",
  okButtonText: "네!"
}).then(() => {
    this.$goto("map")
  console.log("Alert dialog closed");
});
                    //this.$goto('board');
                    })
                .catch(error => {console.log(error)});
                console.log(this.makerinfo)
                console.log(this.$refs.dataform.getPropertyByName('dog_age').valueCandidate);
                
            }
            
        }
    };
</script>