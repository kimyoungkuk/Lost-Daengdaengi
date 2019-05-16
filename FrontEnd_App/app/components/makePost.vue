<template>
    <Page class="page">
        <ActionBar title="Home" class="action-bar" />
        <GridLayout rows = "*,auto">
            <GridLayout row = "0">
                <ScrollView>
                    <RadDataForm :source = "source" :metadata="meta" :groups="groups"></RadDataForm>
                </ScrollView>
            </GridLayout>
            <Button row = "1" @click = "onClick" text = "제출"></Button>
        </GridLayout>
        <!-- <ScrollView>
            <RadDataForm :source="source" :metadata="meta" :groups="groups"></RadDataForm>
        </ScrollView> -->
    </Page>
</template>

<script>
    import { PropertyGroup } from "nativescript-ui-dataform";
    
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
                    }, {
                        "name": "dog_sex",
                        "displayName": "성별",
                        "groupName": "Owner_post",
                        "index": 2,
                    },{
                        "name": "dog_type",
                        "displayName": "견종",
                        "groupName": "Owner_post",
                        "index": 3,
                        "valueProvider" :["말티즈", "시츄", "슈나우져"]
                    }, {
                        "name": "dog_age",
                        "displayName": "나이",
                        "groupName": "Owner_post",
                        "index": 4,
                        "editor" : "Number"
                    }, {
                        "name": "dog_feature",
                        "displayName": "특징",
                        "groupName": "Owner_post",
                        "index": 5,
                    }, {
                        "name": "remark",
                        "displayName": "비고",
                        "groupName": "Owner_post",
                        "index": 6,
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
                        "name": "post_time",
                        "displayName": "게시 시간",
                        "groupName": "Owner_Post",
                        "index": 11,
                        "editor":"DatePicker"
                    },{
                        "name": "post_due",
                        "displayName": "게시 기간",
                        "groupName": "Owner_Post",
                        "index": 12,
                    } ]
                },

                source: {
                    dog_name : "",
                    lost_time : "",
                    dog_sex :"",
                    dog_type :"",
                    dog_age :"",
                    dog_feature:"",
                    remark:"",
                    phone_num:"",
                    lat:"",
                    lng:"",
                    post_time:"",
                    post_due:"",

                }
            };
        }
    };
</script>