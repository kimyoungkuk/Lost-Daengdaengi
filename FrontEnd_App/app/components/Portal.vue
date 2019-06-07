<template>
    <Page class="page" actionBarHidden="true">

        <ActionBar backgroundColor="#44557f" flat="true">
            <StackLayout orientation="vertical" width="100%" height="100%"
                backgroundColor="#44557f">
                <StackLayout backgroundColor="#44557f">
                    <StackLayout #searchRow orientation="horizontal"
                        marginTop="5">
                        <TextField backgroundColor="white" paddingLeft="20"
                            borderRadius="20" v-model="textFieldValue" width="80%"
                            height="40" fontSize="14" hint="Search"></TextField>
                        <Image src="~/assets/images/shape4@3x.png" height="30"
                            width="30" marginLeft="10"></Image>
                    </StackLayout>
                </StackLayout>
            </StackLayout>
        </ActionBar>


        <GridLayout orientation="vertical" width="100%" height="100%" columns="*"
            rows="*,auto">

            <StackLayout col="0" row="0" backgroundColor="#f8f8f8">
                <StackLayout backgroundColor="#44557f" paddingBottom="15"
                    marginTop="-10">
                    <Label text="공지사항(webview)" class="font-weight-bold"
                        color="#FFFFFF" padding="15" fontSize="24"></Label>
                </StackLayout>

                <StackLayout paddingLeft="20" paddingRight="20" paddingTop="20"
                    paddingBottom="5" marginTop="-20" backgroundImage="~/assets/images/layer14@3x.png"
                    borderRadius="5" height="180" width="90%" @tap="showDetails()"
                    stretch="aspectFit" class="album-image">
                    <GridLayout columns="*" rows="auto,*,auto" height="100%">

                        <GridLayout columns="auto,*,auto" rows="auto,auto"
                            col="0" row="2" marginBottom="5">
                            <Label col="0" row="0" class="font-weight-bold"
                                fontSize="18" color="#FFFFFF" text="Hip Hop so far 2018"></Label>
                            <Label col="0" row="1" class="font-weight-bold"
                                fontSize="16" color="#FFFFFF" text="By #Bruno Mars"></Label>
                        </GridLayout>

                    </GridLayout>

                </StackLayout>

                <ScrollView orientation="vertical">
                    <StackLayout>
                        <GridLayout columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="font-weight-bold"
                                paddingLeft="10" fontSize="20" color="#000000"
                                text="찾아주세요"></Label>
                            <Label col="2" row="0" class="font-weight-bold"
                                marginRight="20" fontSize="14" color="#8d8d8d"
                                text="View All (146)"></Label>
                        </GridLayout>


                        <ScrollView orientation="horizontal">
                            <StackLayout orientation="horizontal">
                                <StackLayout margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" backgroundImage="~/assets/images/layer4@3x.png"
                                        borderRadius="5">
                                        <Button horizontalAlignment="right"
                                            marginRight="5" marginTop="80"
                                            width="50" height="20" class="fa btn-rounded-sm"
                                            color="#FFFFFF" backgroundColor="#3b75ff">{{ 'fa-star' | fonticon }}4.9</Button>
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" text="Havana (Remix)"></Label>
                                    <Label fontSize="12" color="#999999" text="2018"></Label>
                                </StackLayout>

                                <StackLayout margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" backgroundImage="~/assets/images/layer5@3x.png"
                                        borderRadius="5">
                                        <Button horizontalAlignment="right"
                                            marginRight="5" marginTop="80"
                                            width="50" height="20" class="fa btn-rounded-sm"
                                            color="#FFFFFF" backgroundColor="#3b75ff">{{ 'fa-star' | fonticon }}4.9</Button>
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" text="Sweetener"></Label>
                                    <Label fontSize="12" color="#999999" text="2018"></Label>
                                </StackLayout>

                                <StackLayout margin="10">
                                    <StackLayout class="album-image" height="110"
                                        backgroundImage="~/assets/images/layer6@3x.png"
                                        borderRadius="5">
                                        <Button horizontalAlignment="right"
                                            marginRight="5" marginTop="80"
                                            width="50" height="20" fontSize="14"
                                            class="fa btn-rounded-sm" color="#FFFFFF"
                                            backgroundColor="#3b75ff">{{ 'fa-star' | fonticon }}4.9</Button>
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" text="Glory Days: The Platinum Edition"></Label>
                                    <Label fontSize="12" color="#999999" text="2018"></Label>

                                </StackLayout>
                            </StackLayout>
                        </ScrollView>

                        <GridLayout columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="font-weight-bold"
                                paddingLeft="10" fontSize="20" color="#000000"
                                text="찾았어요"></Label>
                            <Label col="2" row="0" class="font-weight-bold"
                                marginRight="20" fontSize="14" color="#8d8d8d"
                                text="View All"></Label>
                        </GridLayout>

                        <ScrollView orientation="horizontal">
                            <StackLayout orientation="horizontal">
                                <StackLayout margin="10" height="130" width="110"
                                    backgroundColor="#FFFFFF" borderRadius="5">
                                    <Image src="~/assets/images/shape@3x.png"
                                        width="20" height="20"
                                        horizontalAlignment="right"
                                        marginRight="5"></Image>
                                    <StackLayout horizontalAlignment="center"
                                        verticalAlignment="center">

                                        <Image height="50" width="50" src="~/assets/images/layer7@3x.png"
                                            borderRadius="50"></Image>
                                        <Label fontSize="14" class="font-weight-bold"
                                            color="#000000" text="Bruno Mars"></Label>
                                        <Label fontSize="12" color="#999999"
                                            text="228 Songs"
                                            horizontalAlignment="center"
                                            verticalAlignment="center"></Label>
                                    </StackLayout>

                                    <Button width="75" class="btn-rounded-lg"
                                        text="View All" textTransform="none"
                                        marginBottom="5" backgroundColor="#89acff"
                                        color="#FFFFFF" @tap="onButtonTap()"></Button>
                                </StackLayout>

                                <StackLayout margin="10" height="130" width="110"
                                    backgroundColor="#FFFFFF" borderRadius="5">
                                    <Image src="~/assets/images/shape@3x.png"
                                        width="20" height="20"
                                        horizontalAlignment="right"
                                        marginRight="5"></Image>
                                    <StackLayout horizontalAlignment="center"
                                        verticalAlignment="center">
                                        <Image height="50" width="50" src="~/assets/images/layer8@3x.png"
                                            borderRadius="50"></Image>
                                        <Label fontSize="14" class="font-weight-bold"
                                            color="#000000" text="Ariana Grande"></Label>
                                        <Label fontSize="12" color="#999999"
                                            text="185 Songs"
                                            horizontalAlignment="center"
                                            verticalAlignment="center"></Label>

                                    </StackLayout>
                                    <Button width="75" class="btn-rounded-lg"
                                        text="View All" textTransform="none"
                                        marginBottom="5" backgroundColor="#89acff"
                                        color="#FFFFFF" @tap="onButtonTap()"></Button>
                                </StackLayout>

                                <StackLayout margin="10" height="130" width="110"
                                    backgroundColor="#FFFFFF" borderRadius="5">
                                    <Image src="~/assets/images/shape@3x.png"
                                        width="20" height="20"
                                        horizontalAlignment="right"
                                        marginRight="5"></Image>
                                    <StackLayout horizontalAlignment="center"
                                        verticalAlignment="center">
                                        <Image height="50" width="50" src="~/assets/images/layer9@3x.png"
                                            borderRadius="50"></Image>
                                        <Label fontSize="14" class="font-weight-bold"
                                            color="#000000" text="Big Sean"></Label>
                                        <Label fontSize="12" color="#999999"
                                            text="178 Songs"
                                            horizontalAlignment="center"
                                            verticalAlignment="center"></Label>
                                    </StackLayout>
                                    <Button width="75" class="btn-rounded-lg"
                                        text="View All" textTransform="none"
                                        marginBottom="5" backgroundColor="#89acff"
                                        color="#FFFFFF" @tap="onButtonTap()"></Button>
                                </StackLayout>

                            </StackLayout>
                        </ScrollView>

                        <GridLayout columns="auto,*,auto" rows="auto">
                            <Label col="0" row="0" class="font-weight-bold"
                                paddingLeft="10" fontSize="20" color="#000000"
                                text="분양 게시물"></Label>
                            <Label col="2" row="0" class="font-weight-bold"
                                marginRight="20" fontSize="14" color="#8d8d8d"
                                text="View All"></Label>
                        </GridLayout>

                        <ScrollView orientation="horizontal">
                            <StackLayout orientation="horizontal">
                                <StackLayout margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" backgroundImage="~/assets/images/layer10@3x.png"
                                        borderRadius="5">
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" text="Wings"></Label>
                                    <Label fontSize="12" color="#999999" text="2018"></Label>
                                </StackLayout>

                                <StackLayout margin="10">
                                    <StackLayout class="album-image" height="110"
                                        width="125" backgroundImage="~/assets/images/layer11@3x.png"
                                        borderRadius="5">
                                    </StackLayout>
                                    <Label fontSize="14" class="font-weight-bold"
                                        color="#000000" text="SAX"></Label>
                                    <Label fontSize="12" color="#999999" text="2018"></Label>
                                </StackLayout>

                                <StackLayout margin="10">
                                    <StackLayout class="album-image" height="110"
                                        backgroundImage="~/assets/images/layer12@3x.png"
                                        borderRadius="5">
                                    </StackLayout>
                                    <Label width="125" fontSize="14" class="font-weight-bold"
                                        color="#000000" textWrap="true" text="You Know I Know"></Label>
                                    <Label fontSize="12" color="#999999" text="2018"></Label>

                                </StackLayout>
                            </StackLayout>
                        </ScrollView>


                    </StackLayout>
                </ScrollView>
            </StackLayout>

            <StackLayout col="0" row="1" orientation="horizontal"
                backgroundColor="#FFFFFF" height="60">
                <GridLayout rows="*" columns="*,*,*,*,*">
                    <Image col="0" row="0" (tap)="onButtonTap()" height="25"
                        width="25" margin="10" src="~/assets/images/shape2@3x.png"></Image>
                    <Image col="1" row="0" (tap)="onButtonTap()" height="25"
                        width="25" margin="10" src="~/assets/images/shape1@3x.png"></Image>
                    <Image col="2" row="0" (tap)="onButtonTap()" height="60"
                        width="60" margin="10" src="~/assets/images/home@3x.png"></Image>
                    <Image col="3" row="0" (tap)="onButtonTap()" height="25"
                        width="25" margin="10" src="~/assets/images/shape3@3x.png"></Image>
                    <Image col="4" row="0" (tap)="onButtonTap()" height="25"
                        width="25" margin="10" src="~/assets/images/icon04@3x.png"></Image>
                </GridLayout>
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
            return {};
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
            }
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