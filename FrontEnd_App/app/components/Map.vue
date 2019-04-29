<template>
    <page>
        <ActionBar title="로스트 댕댕이"/>
        <GridLayout columns="*" rows="*">
            <Label class="message" :text="msg" col="0" row="0"/>
        </GridLayout>
    </Page>

</template>


<script >
  export default {
    data() {
      return {
        msg: '맵화면!'
      }
    },
    methods:{

    }
  }
</script>

<style scoped>
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
