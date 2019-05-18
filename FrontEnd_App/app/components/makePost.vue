<template>
    <Page class="page">
        <ActionBar title="Home" class="action-bar" />
        <GridLayout rows = "*,auto">
            <GridLayout row = "0">
                <ScrollView>
                    <RadDataForm ref = "dataform" :source = "source" :metadata="meta" :groups="groups"></RadDataForm>
                </ScrollView>
            </GridLayout>
            <Button row = "1" @tap = "onClick" text = "제출"></Button>
        </GridLayout>
        <!-- <ScrollView>
            <RadDataForm :source="source" :metadata="meta" :groups="groups"></RadDataForm>
        </ScrollView> -->
    </Page>
</template>

<script>
    import { PropertyGroup } from "nativescript-ui-dataform";
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
                        "name": "dog_name",
                        "displayName": "강아지 이름",
                        "groupName": "Owner_post",
                        "index": 0
                    }, {
                        "name": "lost_time",
                        "displayName": "잃어버린 시간",
                        "groupName": "Owner_post",
                        "index": 1,
                        "editor":"DatePicker",

                    },{
                        "name": "lost_time1",
                        "displayName": "잃어버린 시간",
                        "groupName": "Owner_post",
                        "index": 2,
                        "editor":"TimePicker",
                    }, {
                        "name": "dog_sex",
                        "displayName": "성별",
                        "groupName": "Owner_post",
                        "index": 3,
                    },{
                        "name": "dog_type",
                        "displayName": "견종",
                        "groupName": "Owner_post",
                        "index": 4,
                        // "valueProvider" :["말티즈", "시츄", "슈나우져"]
                    }, {
                        "name": "dog_age",
                        "displayName": "나이",
                        "groupName": "Owner_post",
                        "index": 5,
                        // "editor" : "Stepper"
                    }, {
                        "name": "dog_feature",
                        "displayName": "특징",
                        "groupName": "Owner_post",
                        "index": 6,
                    }, {
                        "name": "remark",
                        "displayName": "비고",
                        "groupName": "Owner_post",
                        "index": 7,
                    }, {
                        "name": "phone_num",
                        "displayName": "연락처",
                        "groupName": "Owner_Post",
                        "index": 8,
                    }, {
                        "name": "lat",
                        "displayName": "위도",
                        "groupName": "Owner_Post",
                        "index": 9,
                    },{
                        "name": "lng",
                        "displayName": "경도",
                        "groupName": "Owner_Post",
                        "index": 10,
                    },{
                        "name": "posted_time",
                        "displayName": "게시 시간",
                        "groupName": "Owner_Post",
                        "index": 11,
                        "editor":"DatePicker"
                    },{
                        "name": "posted_due",
                        "displayName": "게시 기간",
                        "groupName": "Owner_Post",
                        "index": 12,
                        "editor":"DatePicker",
                    } ]
                },

                source: {
                    dog_name : "",
                    lost_time : "",
                    lost_time1 : "",
                    dog_sex :"",
                    dog_type :"",
                    dog_age :"",
                    dog_feature:"",
                    remark:"",
                    phone_num:"",
                    lat:"",
                    lng:"",
                    posted_time:"",
                    posted_due:"",

                }
            };
        },

        methods :{
            onClick(args){
                console.log(this.$refs.dataform.getPropertyByName('phone_num').valueCandidate);
                axios.post('http://55913c1c.ngrok.io/api/owner_post_create',{
                    phone_num : this.$refs.dataform.getPropertyByName('phone_num').valueCandidate,
                    dog_name : this.$refs.dataform.getPropertyByName('dog_name').valueCandidate,
                    lost_time : this.$refs.dataform.getPropertyByName('lost_time').valueCandidate+" " +this.$refs.dataform.getPropertyByName('lost_time1').valueCandidate,
                    dog_sex :this.$refs.dataform.getPropertyByName('dog_sex').valueCandidate,
                    dog_type :this.$refs.dataform.getPropertyByName('dog_type').valueCandidate,
                    dog_age :this.$refs.dataform.getPropertyByName('dog_age').valueCandidate,
                    dog_feature:this.$refs.dataform.getPropertyByName('dog_feature').valueCandidate,
                    remark:this.$refs.dataform.getPropertyByName('remark').valueCandidate,
                    lat:this.$refs.dataform.getPropertyByName('lat').valueCandidate,
                    lng:this.$refs.dataform.getPropertyByName('lng').valueCandidate,
                    posted_time:this.$refs.dataform.getPropertyByName('posted_time').valueCandidate,
                    posted_due:this.$refs.dataform.getPropertyByName('posted_due').valueCandidate,
                })
                .then(res => {
                    console.log(res.data);
                    })
                .catch(error => {console.log(error)});
                console.log(this.makerinfo)
                console.log(this.$refs.dataform.getPropertyByName('dog_age').valueCandidate);
            }
            
        }
    };
</script>