<template>
	<page actionBarHidden="true" backgroundSpanUnderStatusBar="true">
		<!-- @loaded="onLoaded" -->

		<GridLayout rows="auto,auto,*,auto" columns="auto">

			<GridLayout row="0" ref="navStatusBar" class="navStatusBar" backgroundColor="#bd2122" verticalAlignment="top" height="40"
			 width="100%" rows="auto" columns="*,auto,auto,auto">
				<Label col="0" row="0" text="게시판" class="status-title"></Label>
					<Image col="1" row="0" @tap="search" horizontalAlignment="right" class="status-img"
							src="~/assets/images/search.png" />
					<Image col="2" row="0" @tap="bell" horizontalAlignment="right" class="status-img"
							src="~/assets/images/bell.png" />
					<Image horizontalAlignment="right" stretch="aspectFill" col="3"
							row="0" class="status-profile" src="~/assets/images/me.jpg" />
			</GridLayout>

			<GridLayout  row="1" ref="navTab" class="navTab" verticalAlignment="top" height="50"
					width="100%"  rows="auto" columns="auto,auto,auto">

					<GridLayout class="tabview" :class="selectedTabview==0?'active':''"
							@tap="popular" rows="*,auto" cols="auto" col="0" row="0"
							width="33%">
							<Image v-show="selectedTabview==0" row="0" class="navIcon"
									:src="selectedTabview==0?'~/assets/images/popular.png':''"/>
							<Label :class="selectedTabview==0?'active':''" row="1"
									text="게시판" class="tabviewText"></Label>
					</GridLayout>
					<GridLayout class="tabview" :class="selectedTabview==1?'active':''"
							@tap="showCategory" rows="*,auto" cols="auto" col="1" row="0"
							width="34%">
							<Image v-show="selectedTabview == 1" row="0" class="navIcon"
									:src="selectedTabview==1?'~/assets/images/category.png':''"/>
							<Label :class="selectedTabview==1?'active':''" row="1"
									text="카테고리" class="tabviewText"></Label>							
					</GridLayout>
					<GridLayout class="tabview" :class="selectedTabview==2?'active':''"
							@tap="showPromos" rows="*,auto" cols="auto" col="2" row="0"
							width="33%">
							<Image v-show="selectedTabview == 2" row="0" class="navIcon"
									:src="selectedTabview==2?'~/assets/images/category.png':''"/>
							<Label :class="selectedTabview==2?'active':''" row="1"
									text="후기" class="tabviewText"></Label>							
					</GridLayout>
			</GridLayout>

			<GridLayout v-show="selectedTabview == 0" row="2" width="100%" backgroundColor="white">
				<ListView ref="listview" separatorColor="transparent" for="item in items" :key="index">
					<v-template>
						<item :item="item" @clicked="showItem(item)" />
					</v-template>
				</ListView>
			</GridLayout>

			<GridLayout v-show="selectedTabview == 1" row="2" width="100%" backgroundColor="white">		
				<ListView ref="listview" separatorColor="transparent" for="item in itemsCategory" :key="index">
					<v-template>
						<Category :item="item"> </Category>
					</v-template>
				</ListView>
			</GridLayout>

			<GridLayout v-show="selectedTabview == 2" row="2" width="100%" backgroundColor="white">		
			</GridLayout>

			<navBottom row="3" />

		</GridLayout>
</page>
</template>
<script>
	// import { SwissArmyKnife } from "nativescript-swiss-army-knife";
	import { isIOS, isAndroid } from 'tns-core-modules/platform'
	import navBottom from "./custom/navBottom";
	import Item from "./custom/item";
	import Category from "./custom/category";
	import PostDetails from "./PostDetails";

	const gestures = require("ui/gestures"); 
	const app = require("application");

export default {
	components: {
		navBottom,
		Item,
		Category
	},
	computed: {
		itemsCategory(){
			return this.category.slice().reverse();
		}
	},

	mounted () {
		// SwissArmyKnife.setAndroidStatusBarColor("#b51213");
	},
	data() {
		return {
			lastDelY: 0,
			headerCollapsed: false,
			selectedTab: 0,
			selectedTabview: 0,
			items: [{
				name: "제발 찾아주세요 ㅠㅠ",
				cover: "~/assets/images/강아지2.PNG",
				images: [
						// {src: "~/assets/images/food/burger/burger1.jpg"},
						// {src: "~/assets/images/food/burger/burger2.jpg"},
						// {src: "~/assets/images/food/burger/burger3.jpg"},
						// {src: "~/assets/images/food/burger/burger4.jpg"},
						// {src: "~/assets/images/food/burger/burger5.jpg"},
						// {src: "~/assets/images/food/burger/burger6.jpg"}
					],
				category: "찾아주세요",
				categoryTag: "#2D9CDB",
				price: "300.00",
				likes: 987,
				isLike: false,
				isFavorite: true,
				comments: 13,
				rating: "아직 찾는중이에요...",
				description: "a"
			},
			{
				name: "찾아주세요ㅠㅠ....",
				cover: "~/assets/images/강아지3.PNG",
				images: [
					// {src: "~/assets/images/food/pancake/pancake1.jpg"},
					// {src: "~/assets/images/food/pancake/pancake2.jpg"},
					// {src: "~/assets/images/food/pancake/pancake3.jpg"},
					// {src: "~/assets/images/food/pancake/pancake4.jpg"},
					// {src: "~/assets/images/food/pancake/pancake5.jpg"},
					// {src: "~/assets/images/food/pancake/pancake6.jpg"}
				],
				category: "찾아주세요",
				categoryTag: "#e4ce0d",
				price: "230.00",
				likes: 891,
				isLike: true,
				isFavorite: true,
				comments: 7,
				rating: "아직 찾는중이에요...",
				description: "a"
			},
			{
				name: "...잃어버렸어요 ..",
				cover: "~/assets/images/말티즈1.PNG",
				images: [
					// {src: "~/assets/images/food/cake/cake1.jpg"},
					// {src: "~/assets/images/food/cake/cake2.jpg"},
					// {src: "~/assets/images/food/cake/cake3.jpg"},
					// {src: "~/assets/images/food/cake/cake4.jpg"}
				],
				category: "찾아주세요",
				categoryTag: "#27AE60",
				price: "300.00",
				likes: 730,
				isLike: true,
				isFavorite: true,
				comments: 11,
				rating: "아직 찾는중이에요...",
				description: "a"
			},
			],
			category: [
			{
				// cover: "~/assets/images/food/burger640.jpg",
				category: "찾아주세요",
				count: "3",
			},
			{
				// cover: "~/assets/images/food/pancake640.jpg",
				category: "찾았어요",
				count: "0",
			},
			]
		};
	},
	methods: {
		search(){
			console.log('search')
		},
		bell(){
			console.log('bell')
		},
		showItem(payload) {
			this.$navigateTo(PostDetails,{
				props: {
					item: payload
				},
				animated: true,
				transition: {
					name: "slideTop",
					duration: 380,
					curve: "easeIn"
				}
			})
		},
		
		popular() {
			this.selectedTabview = 0;
		},
		showCategory() {
			this.selectedTabview = 1;
		},
		showPromos() {
			this.selectedTabview = 2;
		},
		home() {
			this.selectedTab = 0;
		},
		cart() {
			this.selectedTab = 1;
		},
		history() {
			this.selectedTab = 2;
		},
		about() {
			this.selectedTab = 3;
		}
	}
};
</script>

<style>
.tabview.active {
	border-bottom-color: white;
	border-bottom-width: 3;
	margin: 0;
	height: 50;
}
.tabviewText {
	margin-top: 15;
	margin-bottom: 5;
	font-size: 13;
	color: #d8d2d2;
	horizontal-align: center;
}
.tabviewText.active {
	margin-top: 0;
	margin-bottom: 5;
	font-weight: bold;
	color: white;
	vertical-align: center;
}
.navTab {
	background-color: #bd2122;
}
.navTabview {
	background-color: blue;
}
.status-img {
	margin-top: 4;
	margin-right: 20;
	width: 30;
	height: 30;
}
.status-profile {
	border-width: 1;
	border-color: #ffffff;
	background-color: #f1ebeb;
	border-radius: 50%;
	margin-top: 4;
	margin-right: 15;
	width: 30;
	height: 30;
}
.status-title {
	color: white;
	font-size: 18;
	margin-left: 15;
	margin-top: 8;
	horizontal-align: left;
	vertical-align: center;
}
</style>