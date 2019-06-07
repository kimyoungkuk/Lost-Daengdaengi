<template>
	<Page class="page" actionBarHidden="true" backgroundSpanUnderStatusBar="true">

		<!-- <ActionBar flat="true" backgroundColor="#FFFFFF" color="#000000">
		</ActionBar> -->

		<GridLayout orientation="vertical" width="100%" height="100%" columns="*" rows="*,auto" :marginTop='isIOS ? "-20" : ""'>

			<StackLayout col="0" row="0" backgroundColor="#f8f8f8">
				<GridLayout id="detail-page-background" columns="*" rows="auto,*,auto" height="200">
					<GridLayout columns="auto,*,auto" rows="auto" col="0" row="0">
						<Image col="0" row="0" marginLeft="20" marginTop="10" height="25" width="35" @tap="$navigateBack()" src="~/assets/images/shape5@3x.png"></Image>
						<Button col="2" row="0" class="btn btn-rounded-sm" padding="5" textTransform="none"
												backgroundColor="#FFFFFF" color="#3b75ff" text="Make a Sponsor"
												fontSize="12" height="25"></Button>
								</GridLayout>
								<GridLayout columns="auto,*,auto" rows="auto" col="0" row="2"
										marginBottom="20">
										<Label col="0" row="0" class="font-weight-bold" paddingLeft="20"
												fontSize="30" color="#FFFFFF" text="Taylor Swift"></Label>
										<Image col="2" row="0" marginRight="10" height="45" width="45"
												src="~/assets/images/shape7@3x.png"></Image>
								</GridLayout>
						</GridLayout>

						<Label class="font-weight-bold" marginTop="10" paddingLeft="10" fontSize="20" color="#333333" text="Top Songs"></Label>

						<ListView class="list-group" for="item in listViewData" :key="index" height="500" backgroundColor="#f8f8f8">
							<v-template>
								<GridLayout orientation="horizontal" class="list-group-item"
												rows="auto" columns="auto,*,auto">
												<Image col="0" row="0" :src="item.imageUrl" height="75"
														width="75"></Image>
												<StackLayout col="1" row="0" marginLeft="15">
														<Label marginTop="5" paddingRight="5" :text="item.title"
																class="list-group-item-heading font-weight-bold"
																color="#333333"></Label>
														<Label marginTop="5" :text="item.artist" color="#999999"></Label>
														<Label marginTop="5" :text="item.year" color="#999999"></Label>
												</StackLayout>
												<Label col="2" row="0" horizontalAlignment="right" color="#b9b9b9"
														fontSize="24" paddingRight="5" class="fa" > {{ 'fa-ellipsis-v' | fonticon }} </Label>
								</GridLayout>
							</v-template>
						</ListView>
								
				</StackLayout>
				
				<StackLayout col="0" row="1" orientation="horizontal" backgroundColor="#FFFFFF"
						height="60">
						<GridLayout rows="*" columns="*,*,*,*,*">
								<Image col="0" row="0" (tap)="onButtonTap()" height="25" width="25"
										margin="10" src="~/assets/images/shape2@3x.png"></Image>
								<Image col="1" row="0" (tap)="onButtonTap()" height="25" width="25"
										margin="10" src="~/assets/images/shape1@3x.png"></Image>
								<Image col="2" row="0" (tap)="onButtonTap()" height="60" width="60"
										margin="10" src="~/assets/images/home@3x.png"></Image>
								<Image col="3" row="0" (tap)="onButtonTap()" height="25" width="25"
										margin="10" src="~/assets/images/shape3@3x.png"></Image>
								<Image col="4" row="0" (tap)="onButtonTap()" height="25" width="25"
										margin="10" src="~/assets/images/icon04@3x.png"></Image>
						</GridLayout>
				</StackLayout>


		</GridLayout>

	</Page>
</template>

<script>
import { isIOS, isAndroid } from 'tns-core-modules/platform'
export default {
	created() {
		console.log('is IOS platform: ' + isIOS)
		console.log('is Android platform: ' + isAndroid)
	},
	data() {
		return {
			// isIOS: false,
			listViewData: [
			{
					title: "I Don't Wanna Live Forever (Fifty Shades of Grey)",
					artist: "Taylor Swift, Zayn Malik",
					year: "2016",
					imageUrl: "~/assets/images/layer21@3x.png"
			},
			{
					title: "Blank Space",
					artist: "Taylor Swift",
					year: "2014",
					imageUrl: "~/assets/images/layer20@3x.png"
			},
			{
					title: "End Game",
					artist: "Taylor Swift, Ed Sheeran, Future",
					year: "2017",
					imageUrl: "~/assets/images/layer19@3x.png"
			},
			{
					title: "Love Story",
					artist: "Taylor Swift",
					year: "2009",
					imageUrl: "~/assets/images/layer22@3x.png"
			},
			{
					title: "Everything Has Changed",
					artist: "Taylor Swift, Ed Sheeran",
					year: "2012",
					imageUrl: "~/assets/images/layer23@3x.png"
			},
			{
					title: "Teardrops On My Guitar",
					artist: "Taylor Swift",
					year: "2006",
					imageUrl: "~/assets/images/layer24@3x.png"
			},
	]
		}
	},
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

#detail-page-background{        
  background-image: url("~/assets/images/layer18.png");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
</style>