<template>
	<Page class="page" actionBarHidden="true"> 
		<ScrollView ref="scrollView" @scroll="onScroll">
			<StackLayout>
				<StackLayout ref="topView" height="350" style="background-image: url('~/assets/images/owner.jpg'); background-repeat: no-repeat; background-position: center; background-size: cover;">
					<!-- this is the header for collapsing --->
					<!-- Note: this can be any type of layout you want -->
					<!-- <Label text="반려견을 잃어버리셨나요?" color="black" textAlignment="center" fontSize="25" marginTop="1" /> -->
				</StackLayout>
				<StackLayout width="100%" backgroundColor="white" padding="10">
					<!--Add your page content here-->
                    <Label textWrap="true" text="이 앱을 통해 잃어버린 반려견을 등록합니다 ..." class="h2 description-label" />
                    <Label textWrap="true" class="p-10" text="1. 게시글을 Map과 연동"/>
					<Label textWrap="true" class="p-10" text="반려견을 어떻게 찾을 수 있나요? 게시글 등록을 완료하면 Map 상에 게시글이 Marker로 표시되어 보다 쉽게 발견자가 반려견을 알아보고 연락을 취할 수 있습니다. 발견자의 게시글 또한 Map을 거리 기반의 검색으로 잃어버린 장소부터 쉽게 찾아볼 수 있습니다."/>
                    <Label textWrap="true" class="p-10" text="2. 유기견 보호소 연락"/>
					<Label textWrap="true" class="p-10" text="반려견을 어디부터 찾아봐야 하나요? 전국의 유기견 보호소를 100% 커버하는 LDAPP을 통해 주변 유기견 보호소부터 연락을 취하세요."/>
                    <Label textWrap="true" class="p-10" text="3. 반려견을 더 빨리 찾기 위한 꿀팁"/>
					<Label textWrap="true" class="p-10" text="반려견을 찾기 위해 당장 무엇부터 시작해야 하나요? LDAPP에서 제공하는 꿀팁을 참고하세요."/>
                    <Label textWrap="true" class="p-10" text="주인을 찾지 못한 유기견은 큰 사고를 당할 위험이 높으며 보호소에서 주인을 찾지 못한 반려견은 한 달내로 안락사 처리됩니다. LDAPP을 통해 여러분의 소중한 가족을 하루 빨리 찾으세요."/>
                    <Label textWrap="true" text="먼저, 버튼을 눌러 반려견을 잃어버린 위치를 알려주세요." class="h2 description-label" />
                    <Button class="btn mybtn" row = "1" text = "위치 선택" height="50" width="100" @tap ="onTap_Loc"></Button>
				</StackLayout>
			</StackLayout>
		</ScrollView>
	</Page>
</template>

<script>
export default {
  methods: {
        onTap_Loc(args){
        this.$store.state.CurrentPostType = true;
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