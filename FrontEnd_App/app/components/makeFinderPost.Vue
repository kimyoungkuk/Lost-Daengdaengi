<template>
	<Page class="page" actionBarHidden="true"> 
		<ScrollView ref="scrollView" @scroll="onScroll">
			<StackLayout>
				<StackLayout ref="topView" height="425" style="background-image: url('~/assets/images/finder.jpg'); background-repeat: no-repeat; background-position: center; background-size: cover;">
					<!-- this is the header for collapsing --->
					<!-- Note: this can be any type of layout you want -->
					<Label class="font-weight-bold" text="유기견을 발견하셨나요?" color="white" textAlignment="center" fontSize="25" marginTop="25" />
				</StackLayout>
				<StackLayout width="100%" backgroundColor="white" padding="10">
					<!--Add your page content here-->
                    <Label textWrap="true" text="이 앱을 통해 유기견을 제보합니다 ..." class="h2 description-label" />
                    <Label textWrap="true" class="p-10" text="1. 유기견 보호소 추천"/>
					<Label textWrap="true" class="p-10" text="발견한 유기견을 어디에 맡겨야 하나요? 유기견을 보호할 수 있는 가장 가까운 유기견 보호소를 추천해주고 해당 장소까지 안내합니다."/>
                    <Label textWrap="true" class="p-10" text="2. 머신 러닝을 이용한 견종 분류"/>
					<Label textWrap="true" class="p-10" text="발견한 유기견의 견종을 모르시나요? 발견한 유기견의 견종을 카메라로 촬영하면 자동으로 견종을 분류 및 추천해줍니다."/>
                    <Label textWrap="true" class="p-10" text="3. 게시글을 Map과 연동"/>
					<Label textWrap="true" class="p-10" text="견주를 어떻게 찾을 수 있나요? 게시글 등록을 완료하면 Map 상에 게시글이 Marker로 표시되어 보다 쉽게 견주가 유기견을 찾아볼 수 있습니다."/>
                    <Label textWrap="true" class="p-10" text="주인을 찾지 못한 유기견은 한 달내로 안락사 처리됩니다. 여러분의 소중한 제보가 하루 빨리 유기견이 가족의 품에 돌아갈 수 있도록 도와줍니다."/>
                    <Label textWrap="true" text="먼저, 버튼을 눌러 발견한 유기견의 모습을 알려주세요." class="h2 description-label" />
                    <Button class="btn mybtn" row = "1" text = "유기견 제보" height="50" width="100" @tap="$goto('camera')"></Button>
                    <!-- onTap_Loc -->
				</StackLayout>
			</StackLayout>
		</ScrollView>
	</Page>
</template>

<script>
export default {
  methods: {
        onTap_Loc(args){
        this.$store.state.CurrentPostType = false;
        this.$goto('select_Loc');
    },
    onScroll: function () {
      //access to the native event
      const scrollView = this.$refs.scrollView.nativeView;
      const topView = this.$refs.topView.nativeView;

      // if the offset is less than the height of the header.
      if (scrollView.verticalOffset < 250) {
        const offset = scrollView.verticalOffset / 1.65; // you can adjust this number to make the parallax more subtle or dramatic
        if (scrollView.ios) {
          // iOS adjust the position with an animation to create a smother scrolling effect. 
          topView.animate({ translate: { x: 0, y: offset } }).then(() => { }, () => { });
        } else {
          // Android, animations are jerky so instead just adjust the position without animation.
          topView.translateY = Math.floor(offset);
        }
      }
    }
  }
};
</script>

<style scoped>
      .mybtn{
      color: #ffffff;
      background-color: #FA7268;
    }
</style>