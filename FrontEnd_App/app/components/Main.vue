<template>
    <Page>
        <ActionBar title="Lost DaengDaengi Main"/>
        <FlexboxLayout class="page" >
          <StackLayout>
            <Image class="logo" src="~/assets/images/DaengDaengi.png" horizontalAlignment="center" stretch="none" />
            <Button text="로그인" height="50" width="100" @tap="$goto('login')" />
            <Button text="게시판" height="50" width="100" @tap="$goto('board')" />
            <Button text="맵뷰" height="50" width="100" @tap="$goto('map')" />
            <Button text="카메라" height="50" width="100" @tap="$goto('camera')" />
            <Label class="message" :text="msg" col="0" row="0"/>
          </StackLayout>
        </FlexboxLayout >
    </Page>
</template>

<script >
  export default {
    data() {
      return {
        msg: 'Lost Daengdaengi!'
      }
    },
    methods:{

    }
  }
</script>

<style scoped>
	.page {
		align-items: center;
		flex-direction: column;
  }
    ActionBar {
        background-color: #53ba82;
        color: #ffffff;
    }

    .message {
        vertical-align: center;
        text-align: center;
        font-size: 20;
        color: #333333;
    }
</style>
