<template>
    <Page class="page" @loaded="loaded">
        <ActionBar flat="true" title="로스트 댕댕이">
            <NavigationButton icon = "~/assets/images/baseline_menu_black_18dp.png" @tap="openDrawer"/>
           <ActionItem @tap="$goto('makeFinderPost')">
                <button text="찾았어요" class="btn mybtn font-weight-bold" android:horizontalAlignment="left" >/>
                </button>
            </ActionItem>
            <ActionItem @tap="$goto('makeOwnerPost')" >
                <button text="찾아주세요" class="btn mybtn font-weight-bold" android:horizontalAlignment="right">/>
                </button>
            </ActionItem>
        </ActionBar>


        <GridLayout orientation="vertical" width="100%" height="100%" columns="*"
            rows="*,auto" >
          
            <StackLayout col="0" row="0" backgroundColor="#ffffff">
                  <Webview src="http://202.30.31.91/aboutus" id="myWebView" height="auto"/>
                    <Button class="font-weight-bold fas fa-search-location"
                                fontSize="25" color="#FA7268" backgroundColor="#ffffff" 
                                :text="'\uf689' + '내 주변 지도로 확인하기'" @tap="$goto('map')" style="text-align: center;"></Button>
                <ScrollView orientation="vertical">
                    <StackLayout>
                        <GridLayout backgroundColor="#FA7268"  columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="fas fa-search font-weight-bold"
                                paddingLeft="10" fontSize="16" color="#ffffff"
                                :text="'\uf002' + '찾아주세요'" @tap="viewAll_Owner">></Label>
                            <Label col="2" row="0" class="font-weight-bold fas fa-list"
                                marginRight="20" fontSize="16" color="#ffffff"
                                :text="'\uf03a' + '모두보기'" @tap="viewAll_Owner"></Label>
                        </GridLayout>


                        <ScrollView orientation="horizontal">
                            <StackLayout orientation="horizontal">
                                <StackLayout @tap="viewDetail_Owner" id="Owner_1" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Owner_imgSrc[0]"
                                        borderRadius="5">
                                     
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Owner_txtSrc[0]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Owner_dtimeSrc[0]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout @tap="viewDetail_Owner" id="Owner_2" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Owner_imgSrc[1]"
                                        borderRadius="5">
                                     
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Owner_txtSrc[1]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Owner_dtimeSrc[1]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout @tap="viewDetail_Owner" id="Owner_3" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Owner_imgSrc[2]"
                                        borderRadius="5">
                                   
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Owner_txtSrc[2]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Owner_dtimeSrc[2]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>

                                  <StackLayout @tap="viewDetail_Owner" id="Owner_4" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Owner_imgSrc[3]"
                                        borderRadius="5">
                                   
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Owner_txtSrc[3]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Owner_dtimeSrc[3]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>
                            </StackLayout>
                        </ScrollView>

                        <GridLayout backgroundColor="#FA7268" columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="fas fa-search font-weight-bold "
                                paddingLeft="10" fontSize="16" color="#ffffff"
                                :text="'\uf002'+ '찾았어요'" @tap="viewAll_Finder"></Label>
                            <Label col="2" row="0" class="font-weight-bold fas fa-list"
                                marginRight="20" fontSize="16" color="#ffffff"
                                :text="'\uf03a' + '모두보기'" @tap="viewAll_Finder"></Label>
                        </GridLayout>

                        <ScrollView orientation="horizontal">
                            <StackLayout orientation="horizontal">
                                <StackLayout @tap="viewDetail_Finder" id="Finder_1" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Finder_imgSrc[0]"
                                        borderRadius="5">
                                        
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Finder_txtSrc[0]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finder_dtimeSrc[0]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout  @tap="viewDetail_Finder" id="Finder_2" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Finder_imgSrc[1]"
                                        borderRadius="5">
                                     
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Finder_txtSrc[1]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finder_dtimeSrc[1]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout  @tap="viewDetail_Finder" id="Finder_3" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Finder_imgSrc[2]"
                                        borderRadius="5">
                                     
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Finder_txtSrc[2]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finder_dtimeSrc[2]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>

                                  <StackLayout  @tap="viewDetail_Finder" id="Finder_4" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Finder_imgSrc[3]"
                                        borderRadius="5">
                                    
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Finder_txtSrc[3]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finder_dtimeSrc[3]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>
                            </StackLayout>
                        </ScrollView>

                        <GridLayout backgroundColor="#FA7268" columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="font-weight-bold"
                                paddingLeft="10" fontSize="16" color="#ffffff"
                                text="분양 게시물" @tap="viewAll_Adopt"></Label>
                            <Label col="2" row="0" class="font-weight-bold fas fa-list"
                                marginRight="20" fontSize="16" color="#ffffff"
                                :text="'\uf03a' + '모두보기'" @tap="viewAll_Adopt"></Label>
                        </GridLayout>

                        <ScrollView orientation="horizontal">
                            <StackLayout orientation="horizontal">
                                <StackLayout  @tap="viewDetail_Adopt" id="Adopt_1" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Adopt_imgSrc[0]"
                                        borderRadius="5">
                                      
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Adopt_txtSrc[0]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Adopt_dtimeSrc[0]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout @tap="viewDetail_Adopt" id="Adopt_2" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Adopt_imgSrc[1]"
                                        borderRadius="5">
                                     
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Adopt_txtSrc[1]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Adopt_dtimeSrc[1]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout  @tap="viewDetail_Adopt" id="Adopt_3" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Adopt_imgSrc[2]"
                                        borderRadius="5">
                                      
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Adopt_txtSrc[2]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Adopt_dtimeSrc[2]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>

                                  <StackLayout @tap="viewDetail_Adopt" id="Adopt_4" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Adopt_imgSrc[3]"
                                        borderRadius="5">
                                    
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Adopt_txtSrc[3]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Adopt_dtimeSrc[3]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>
                            </StackLayout>
                        </ScrollView>

                        <GridLayout backgroundColor="#FA7268" columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="font-weight-bold"
                                paddingLeft="10" fontSize="16" color="#ffffff"
                                text="반환완료" @tap="viewAll_Finish"></Label>
                            <Label col="2" row="0" class="font-weight-bold fas fa-list"
                                marginRight="20" fontSize="16" color="#ffffff"
                                :text="'\uf03a' + '모두보기'" @tap="viewAll_Finish"></Label>
                        </GridLayout>

                        <ScrollView orientation="horizontal">
                            <StackLayout orientation="horizontal">
                                <StackLayout @tap="viewDetail_Finish" id="Finish_1" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Finish_imgSrc[0]"
                                        borderRadius="5">
                                  
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Finish_txtSrc[0]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finish_dtimeSrc[0]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout @tap="viewDetail_Finish" id="Finish_2" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" :backgroundImage="Finish_imgSrc[1]"
                                        borderRadius="5">
                                 
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" :text="Finish_txtSrc[1]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finish_dtimeSrc[1]).format('YYYY-MM-DD')"></Label>
                                </StackLayout>

                                <StackLayout @tap="viewDetail_Finish" id="Finish_3" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Finish_imgSrc[2]"
                                        borderRadius="5">

                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Finish_txtSrc[2]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finish_dtimeSrc[2]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>

                                  <StackLayout @tap="viewDetail_Finish" id="Finish_4" margin="10">
                                    <StackLayout class="album-image" height="110"
                                        :backgroundImage="Finish_imgSrc[3]"
                                        borderRadius="5">
          
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" :text="Finish_txtSrc[3]"></Label>
                                    <Label fontSize="12" color="#999999" :text="$moment(this.Finish_dtimeSrc[3]).format('YYYY-MM-DD')"></Label>

                                </StackLayout>
                            </StackLayout>
                        </ScrollView>


                    </StackLayout>
                </ScrollView>
            </StackLayout>

        </GridLayout>
    </page>
</template>
<script>
    import sideDrawer from '~/mixins/sideDrawer'
    export default {
        mixins: [ sideDrawer ],
        computed: {},
        mounted() {},
        data() {
            return {
                Finder_imgSrc : [],
                Owner_imgSrc :[],
                Finish_imgSrc :[],
                Adopt_imgSrc :[],
                Finder_txtSrc : [],
                Owner_txtSrc :[],
                Finish_txtSrc :[],
                Adopt_txtSrc :[],
                Finder_dtimeSrc : [],
                Owner_dtimeSrc :[],
                Finish_dtimeSrc :[],
                Adopt_dtimeSrc :[],
                Finder_id : [],
                Owner_id :[],
                Finish_id :[],
                Adopt_id :[],


            };
        },
        created(){
            this.$http.get(this.$store.state.API_BACKEND_URL + "/api/ownerPosts/list/portal/",{

            }).then(res=> {
                console.log(res.data);
                for(var i=0;i<4;i++){
                    this.Owner_imgSrc.push(res.data[i].imageurl);
                    this.Owner_txtSrc.push(res.data[i].title);
                    this.Owner_dtimeSrc.push(res.data[i].posted_time);
                    this.Owner_id.push(res.data[i].id);
                }
                
               // this.Owner_imgSrc = res.data;
            });
            this.$http.get(this.$store.state.API_BACKEND_URL + "/api/finderPosts/list/portal/",{

            }).then(res=> {
                for(var i=0;i<4;i++){
                    this.Finder_imgSrc.push(res.data[i].imageurl);
                    this.Finder_txtSrc.push(res.data[i].title);
                    this.Finder_dtimeSrc.push(res.data[i].posted_time);
                    this.Finder_id.push(res.data[i].id);
              }
            });
            this.$http.get(this.$store.state.API_BACKEND_URL + "/api/finishPosts/list/portal/",{

            }).then(res=> {
                for(var i=0;i<4;i++){
                    this.Finish_imgSrc.push(res.data[i].imageurl);
                    this.Finish_txtSrc.push(res.data[i].title);
                    this.Finish_dtimeSrc.push(res.data[i].posted_time);
                    this.Finish_id.push(res.data[i].id);

                }
            });
            this.$http.get(this.$store.state.API_BACKEND_URL + "/adopt/post/list/portal/",{

            }).then(res=> {
                for(var i=0;i<4;i++){
                    this.Adopt_imgSrc.push(res.data[i].imageurl);
                    this.Adopt_txtSrc.push(res.data[i].title);
                    this.Adopt_dtimeSrc.push(res.data[i].posted_time);
                    this.Adopt_id.push(res.data[i].id);

                }
            });
            
        },
        methods: {
             loaded(webargs) {
const page = webargs.object
const webview = page.getViewById('myWebView');
webview.android.getSettings().setDisplayZoomControls(false);
webview.android.getSettings().setBuiltInZoomControls(false);
},  
            onButtonTap() {},
            showDetails() {
                this.$navigateTo(Details, {
                    animated: true,
                    transition: {
                        name: "slideLeft",
                        duration: 250,
                        curve: "easeIn"
                    }
                });
            },
            viewAll_Owner(args){
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/ownerboard"+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewAll_Finder(args){
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finderboard"+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewAll_Adopt(args){
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/adopt/post/list"+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewAll_Finish(args){
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finishboard"+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewDetail_Owner(args){
                var Post_id = args.object.id;
                var Pid_to = 0;
                switch(Post_id){
                    case 'Owner_1':
                        Pid_to = this.Owner_id[0];
                        break;
                    case 'Owner_2':
                        Pid_to = this.Owner_id[1];
                        break;
                    case 'Owner_3':
                        Pid_to = this.Owner_id[2];
                        break;
                    case 'Owner_4':
                        Pid_to = this.Owner_id[3];
                        break;            
                }
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/ownerboard/view/"+Pid_to+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewDetail_Finder(args){
                var Post_id = args.object.id;
                var Pid_to = 0;
                switch(Post_id){
                    case 'Finder_1':
                        Pid_to = this.Finder_id[0];
                        break;
                    case 'Finder_2':
                        Pid_to = this.Finder_id[1];
                        break;
                    case 'Finder_3':
                        Pid_to = this.Finder_id[2];
                        break;
                    case 'Finder_4':
                        Pid_to = this.Finder_id[3];
                        break;            
                }
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finderboard/view/"+Pid_to+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewDetail_Finish(args){ 
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finishboard"+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewDetail_Adopt(args){
                 var Post_id = args.object.id;
                var Pid_to = 0;
                switch(Post_id){
                    case 'Adopt_1':
                        Pid_to = this.Adopt_id[0];
                        break;
                    case 'Adopt_2':
                        Pid_to = this.Adopt_id[1];
                        break;
                    case 'Adopt_3':
                        Pid_to = this.Adopt_id[2];
                        break;
                    case 'Adopt_4':
                        Pid_to = this.Adopt_id[3];
                        break;            
                }
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/adopt/post/detail/"+Pid_to+ "?key=" + this.$store.state.user_key +"&nickname=" +this.$store.state.user_nickname;
                this.$goto('Portal_to_Board');
            },
        }
    };
</script>

<style scoped>
ActionBar {
        background-color: #FA7268;
        color: #ffffff;
    }
    .album-image {
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
    }

    .home-panel {
        vertical-align: center;
        font-size: 20;
        margin: 15;
    }

    .description-label {
        margin-bottom: 15;
    }
    .mybtn{
  color: #FA7268;
  background-color: #FFFFFF;
}

    #searchRow {
        margin-top: 20;
    }
</style>