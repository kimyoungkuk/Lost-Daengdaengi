<template>
    <Page class="page">
        <ActionBar backgroundColor = "#FA7268" class="action-bar">
            <Label class="action-bar-title" backgroundColor = "#FA7268" color = "#ffffff" text="마이페이지"></Label>
             <ActionItem @tap="onTapFin">
                <button text="완료" class="btn btn-primary" backgroundColor="#ffffff" color = "#FA7268" android:horizontalAlignment="right" >/></button>
            </ActionItem>
        </ActionBar>
        
        <stackLayout>
            <label text=""></label>
            <image class="logo" src="~/assets/images/DaengDaengi.png"/>
            <DockLayout width ="250" height="50" backgroundColor="white" stretchLastChild="true">
                <Label class="labels" dock="left" text="닉네임 : "/>
                <Textfield v-model="ChangedNickName" class="TextFields" dock="last child" row="0" columns="0" editable="true" />
            </DockLayout>
            <Label class="fa" height="40" backgroundColor="#FFFFFF" textWrap="true" style="text-align:center">
    <FormattedString>
      <Span class="font-italic font-weight-bold" text="2019 Capstone Design" style="font-size: 24px; color: #FA7268; "/>
    </FormattedString>
  </Label>
    <Label height="30" backgroundColor="#FFFFFF" textWrap="true" style="text-align:center">
    <FormattedString>
      <Span text="Team - Bohemian capsody" fontWeight="bold" style="font-size: 18px; color: #FA7268;"/>
    </FormattedString>
    </Label>
      <Label height="30" backgroundColor="#FFFFFF" textWrap="true" style="text-align:center ">
    <FormattedString>
      <Span text="김영국 | 박신혁 | 박찬영 | 최순원" style="font-size: 16px; background-color:#FA7268; color: #FFFFFF;"/>
    </FormattedString>
  </Label>
        </stackLayout>
    </Page>
</template>


<script >
import { ChangeType } from 'tns-core-modules/data/observable-array/observable-array';

  export default {
    data() {
      return {
        ChangedNickName : this.$store.state.user_nickname,
      }
    },
    methods:{
        onTapFin(args){
            this.$http.post(this.$store.state.API_BACKEND_URL + '/api/users/changeNickname',{
                key : this.ChangedNickName,
                nickname : this.$store.state.user_nickname,
                is_admin : 0,
            }).then(res =>{
                console.log(res.data)
            })
            
        },
    }
  }
</script>


<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
    .labels {
    /* background-color: #bc7474; */
    /* color: whitesmoke; */
    font-size: 15;
    padding: 8;
    /* text-align: center; */
    vertical-align: middle;
    /* width: 90%; */
    }   
	.logo {
		margin-bottom: 12;
		height: 90;
		font-weight: bold;
	}
    .TextFields {
        font-size :15;
        padding : 8;
    }

</style>