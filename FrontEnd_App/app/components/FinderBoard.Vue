<template>
    <Page class="page" actionBarHidden="true">
        <ActionBar title="Home" class="action-bar" />
        <ScrollView>
            <GridLayout>
                <GridLayout row="0" rows="*" columns="50 * 50" class="form">
                </GridLayout>
                <WebView row="1" loaded="onWebViewLoaded" id="myWebView" :src="this.API_WEBVIEW_URL" />
                <Label row="2" text="  " />
            </GridLayout>
        </ScrollView>
    </Page>
</template>

<script>
    export default {
        data() {
            return {
                API_WEBVIEW_URL: this.$store.state.API_WEBVIEW_URL + "/finderboard",
            };
        }
    };
</script>

<style scoped>
    .home-panel {
        vertical-align: center;
        font-size: 20;
        margin: 15;
    }

    .description-label {
        margin-bottom: 15;
    }
</style>