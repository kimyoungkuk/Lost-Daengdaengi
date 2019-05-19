<template>
    <Page class="page">
        <ActionBar title="Home" class="action-bar" />
        <ScrollView>
            <GridLayout rows="75 * 50">
                <GridLayout row="0" rows="*" columns="50 * 50" class="form">
                    <Button class="btn btn-primary btn-active icon" row="0"
                        col="0" text="&#xea44;" tap="goBack" />
                    <TextField row="0" col="1" id="urlField" hint="Enter URL"
                        text=" tftext " returnKeyType="done" returnPress="submit"
                        autocorrect="false" verticalAlignment="center" class="input input-border m-t-0"
                        autocapitalizationType="none" />
                    <Button class="btn btn-primary btn-active icon"
                        row="0" col="2" text="&#xea42;" tap="goForward" />
                </GridLayout>
                <WebView row="1" loaded="onWebViewLoaded" id="myWebView" src="http://192.168.43.210:8080/ownerboard" />
                <Label row="2" text="  " />
            </GridLayout>
        </ScrollView>
    </Page>
</template>

<script>
    export default {
        data() {
            return {};
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