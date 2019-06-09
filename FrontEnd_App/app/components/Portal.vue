<template>
    <Page class="page" actionBarHidden="true">

        <ActionBar backgroundColor="#44557f" flat="true">
            <StackLayout orientation="vertical" width="100%" height="100%"
                backgroundColor="#44557f">
                <StackLayout backgroundColor="#44557f">
                    <StackLayout #searchRow orientation="horizontal"
                        marginTop="5">
                        <TextField backgroundColor="white" paddingLeft="20"
                            borderRadius="20" width="80%"
                            height="40" fontSize="14" hint="Search"></TextField>
                        <Image src="~/assets/images/shape4@3x.png" height="30"
                            width="30" marginLeft="10"></Image>
                    </StackLayout>
                </StackLayout>
            </StackLayout>
        </ActionBar>


        <GridLayout orientation="vertical" width="100%" height="100%" columns="*"
            rows="*,auto" >
          
            <StackLayout col="0" row="0" backgroundColor="#ffffff">
                  <Webview src="http://202.30.31.91/aboutus" height="auto"/>
                <!-- <StackLayout backgroundColor="#44557f" paddingBottom="15"
                    marginTop="-10">
                    <Label text="공지사항(webview)" class="font-weight-bold"
                        color="#FFFFFF" padding="15" fontSize="24"></Label>
                </StackLayout>

                <StackLayout paddingLeft="20" paddingRight="20" paddingTop="20"
                    paddingBottom="5" marginTop="-20" backgroundImage="~/assets/images/layer14@3x.png"
                    borderRadius="5" height="180" width="90%" @tap="showDetails()"
                    stretch="aspectFit" class="album-image">
                    <GridLayout columns="*" rows="auto,*,auto" height="100%">

                        
                        

                    </GridLayout>

                </StackLayout> -->

                <ScrollView orientation="vertical">
                    <StackLayout>
                        <GridLayout backgroundColor="#FA7268"  columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="font-weight-bold"
                                paddingLeft="10" fontSize="20" color="#ffffff"
                                text="찾아주세요" @tap="viewAll_Owner">></Label>
                            <Label col="2" row="0" class="font-weight-bold"
                                marginRight="20" fontSize="14" color="#ffffff"
                                text="모두보기" @tap="viewAll_Owner"></Label>
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
                            <Label col="0" row="0" class="font-weight-bold"
                                paddingLeft="10" fontSize="20" color="#ffffff"
                                text="찾았어요" @tap="viewAll_Finder"></Label>
                            <Label col="2" row="0" class="font-weight-bold"
                                marginRight="20" fontSize="14" color="#ffffff"
                                text="모두보기" @tap="viewAll_Finder"></Label>
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
                                paddingLeft="10" fontSize="20" color="#ffffff"
                                text="분양 게시물" @tap="viewAll_Adopt"></Label>
                            <Label col="2" row="0" class="font-weight-bold"
                                marginRight="20" fontSize="14" color="#ffffff"
                                text="모두보기" @tap="viewAll_Adopt"></Label>
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
                                paddingLeft="10" fontSize="20" color="#ffffff"
                                text="반환완료" @tap="viewAll_Finish"></Label>
                            <Label col="2" row="0" class="font-weight-bold"
                                marginRight="20" fontSize="14" color="#ffffff"
                                text="모두보기" @tap="viewAll_Finish"></Label>
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
    import Details from "./Details";

    export default {
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
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/ownerboard"+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewAll_Finder(args){
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finderboard"+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewAll_Adopt(args){
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/adopt/post/list"+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewAll_Finish(args){
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finishboard"+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
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
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/ownerboard/view/"+Pid_to+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
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
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finderboard/view/"+Pid_to+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
                this.$goto('Portal_to_Board');
            },
            viewDetail_Finish(args){ 
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/finishboard"+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
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
                this.$store.state.Redirect_URL = this.$store.state.API_WEBVIEW_URL + "/adopt/post/detail/"+Pid_to+ "?key=" + this.user_key +"&nickname=" +this.user_nickname;
                this.$goto('Portal_to_Board');
            },
        }
    };
</script>

<style scoped>
    ActionBar {
        background-color: transparent;
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

    #searchRow {
        margin-top: 20;
    }
</style>