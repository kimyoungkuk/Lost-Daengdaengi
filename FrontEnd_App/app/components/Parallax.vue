<template>
	<Page class="page">
        <GridLayout rows="*, auto, auto">
        <GridLayout row="0" rows="*" columns="*, auto">        
                <Mapbox row = "0"
                    accessToken="pk.eyJ1IjoicWtyODE5IiwiYSI6ImNqdjJhMjY1eTIyeDgzeW1mejl4YmZlaWsifQ.1hDcizlwRYzZqUXF6gz6tQ"
                    mapStyle="traffic_day"
                    latitude="37.532600"
                    longitude="127.024612"
                    hideCompass="true"
                    zoomLevel="12"
                    showUserLocation="false"
                    disableZoom="false"
                    disableRotation="false"
                    disableScroll="false"
                    disableTilt="false"
                    @mapReady="onMapReady($event)">
                    
                </Mapbox> 
                <Button row = "1" backgroundColor = "#ffffff" @swipe = "onSwipe" padding = "10"></Button>
                           
        </GridLayout>
		<ScrollView ref="scrollView" @scroll="onScroll">
			<StackLayout>
				<StackLayout ref="topView" height="500">
					<!-- this is the header for collapsing --->
					<!-- Note: this can be any type of layout you want -->
    
					<Label text="Parallax" color="gray" textAlignment="center" fontSize="45" marginTop="40" />
				</StackLayout>
				<StackLayout width="100%" backgroundColor="white" padding="10">
					<!--Add your page content here-->
					<Label textWrap="true" text="Vue + NativeScript Parallax" class="h2 description-label" />
					<Label textWrap="true" class="p-10" text="Tart muffin marshmallow marzipan cake. Brownie liquorice marzipan chupa chups wafer jelly beans liquorice candy cake. Lollipop icing halvah marzipan candy canes liquorice. Sesame snaps brownie dessert chocolate bar wafer brownie. Cupcake gingerbread tiramisu jelly liquorice jujubes gummi bears. Cotton candy marshmallow cotton candy tiramisu jelly sweet caramels marshmallow halvah. Chupa chups muffin candy. Tart topping dessert sweet dessert dragée cake cupcake chupa chups. Gummies tootsie roll dragée jelly beans candy canes jelly-o chocolate carrot cake. Powder jelly beans topping pie danish gummies jelly. jelly-o sesame snaps danish sweet roll marshmallow halvah croissant chupa chups. Cookie gummi bears jelly-o cake marshmallow danish chupa chups cotton candy. Carrot cake marshmallow sweet."
					/>
					<Label textWrap="true" class="p-10" text="Gummi bears carrot cake fruitcake cookie jelly-o jelly beans. Gummi bears jelly beans sugar plum. Marzipan cookie pie wafer cupcake cake. Bonbon tiramisu toffee chocolate bar toffee ice cream gummies. Pastry marshmallow lollipop marshmallow chupa chups tiramisu candy powder. Brownie chupa chups biscuit biscuit bonbon icing pastry. Icing liquorice cupcake gingerbread cupcake. Tiramisu marzipan chocolate bar lollipop gummi bears bonbon. Powder wafer pudding chocolate cake jelly toffee. Halvah carrot cake oat cake sugar plum candy jelly-o. Cookie toffee toffee marzipan lollipop dragée donut. Chupa chups jelly-o candy cotton candy bear claw sweet roll tart."
					/>
					<Label textWrap="true" class="p-10" text="Tart muffin marshmallow marzipan cake. Brownie liquorice marzipan chupa chups wafer jelly beans liquorice candy cake. Lollipop icing halvah marzipan candy canes liquorice. Sesame snaps brownie dessert chocolate bar wafer brownie. Cupcake gingerbread tiramisu jelly liquorice jujubes gummi bears. Cotton candy marshmallow cotton candy tiramisu jelly sweet caramels marshmallow halvah. Chupa chups muffin candy. Tart topping dessert sweet dessert dragée cake cupcake chupa chups. Gummies tootsie roll dragée jelly beans candy canes jelly-o chocolate carrot cake. Powder jelly beans topping pie danish gummies jelly. jelly-o sesame snaps danish sweet roll marshmallow halvah croissant chupa chups. Cookie gummi bears jelly-o cake marshmallow danish chupa chups cotton candy. Carrot cake marshmallow sweet."
					/>
				</StackLayout>
			</StackLayout>
		</ScrollView>
        </GridLayout>
	</Page>
</template>

<script>
export default {
  methods: {
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
