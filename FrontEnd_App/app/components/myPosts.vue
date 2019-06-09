<template>
	<Page class="page" backgroundSpanUnderStatusBar="true">

		<ActionBar title="내가 쓴 게시물" flat="true" backgroundColor="#FA7268" color="#ffffff">
		</ActionBar>

		<GridLayout orientation="vertical" width="100%" height="100%" columns="*" rows="*,auto,auto">

			<StackLayout col="0" row="0" backgroundColor="#f8f8f8">
						<Label class="font-weight-bold" marginTop="10" paddingLeft="10" fontSize="20" backgroundColor="#FA7268" color="#ffffff" text="찾았어요"></Label>

						<ListView class="list-group" for="item in Finder"  height="200" backgroundColor="#f8f8f8">
							<v-template>
								<GridLayout orientation="horizontal" class="list-group-item"
												rows="auto" columns="auto,*,auto">
												<Image col="0" row="0" :src="item.imageurl" height="75"
														width="75"></Image>
												<StackLayout col="1" row="0" marginLeft="15">
														<Label marginTop="5" paddingRight="5" :text="item.title"
																class="list-group-item-heading font-weight-bold"
																color="#333333"></Label>
														<Label marginTop="5" text="찾았어요" color="#999999"></Label>
														<Label marginTop="5" :text="item.posted_time" color="#999999"></Label>
												</StackLayout>
												<Label col="2" row="0" horizontalAlignment="right" color="#b9b9b9"
														fontSize="24" paddingRight="5" class="fa" > {{ 'fa-ellipsis-v' | fonticon }} </Label>
								</GridLayout>
							</v-template>
						</ListView>
						<Label class="font-weight-bold" marginTop="10" paddingLeft="10" fontSize="20" backgroundColor="#FA7268" color="#ffffff" text="찾아주세요"></Label>

						<ListView class="list-group" for="item in Owner"  height="200" backgroundColor="#f8f8f8">
							<v-template>
								<GridLayout orientation="horizontal" class="list-group-item"
												rows="auto" columns="auto,*,auto">
												<Image col="0" row="0" :src="item.imageurl" height="75"
														width="75"></Image>
												<StackLayout col="1" row="0" marginLeft="15">
														<Label marginTop="5" paddingRight="5" :text="item.title"
																class="list-group-item-heading font-weight-bold"
																color="#333333"></Label>
														<Label marginTop="5" text="찾아주세요" color="#999999"></Label>
														<Label marginTop="5" :text="item.posted_time" color="#999999"></Label>
												</StackLayout>
												<Label col="2" row="0" horizontalAlignment="right" color="#b9b9b9"
														fontSize="24" paddingRight="5" class="fa" > {{ 'fa-ellipsis-v' | fonticon }} </Label>
								</GridLayout>
							</v-template>
						</ListView>
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
								
				</StackLayout>
				
				
		</GridLayout>

	</Page>
</template>

<script>
// import { isIOS, isAndroid } from 'tns-core-modules/platform'
export default {
	created() {
		// console.log('is IOS platform: ' + isIOS)
		// console.log('is Android platform: ' + isAndroid)
		this.$http.get(this.$store.state.API_BACKEND_URL + "/api/myPosts"+"?key=" + this.$store.state.user_key,{

		}).then(res => {
			this.Finder = res.data.finder
			this.Owner = res.data.owner
			// listViewData = Finder + 
			console.log(this.listViewData)
			console.log(res.data)
		})
	},
	data() {
		return {
			// isIOS: false,
			Finder: [
				
			],
			Owner : [],
			listViewData : []
		}
	},
	//api/myPosts
	methods: {
		onItemTap(){

		}
	},
	
	};
</script>
<style scoped>
ActionBar{
  background-color:transparent;
}


</style>