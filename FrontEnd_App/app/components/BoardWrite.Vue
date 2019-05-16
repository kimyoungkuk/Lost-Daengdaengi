<template>
	<Page class="page">
		<ActionBar title="Dialogs" class="action-bar" />
		<ScrollView>
			<StackLayout class="home-panel">
				<Label textWrap="true" class="body m-20" text="The following shows a few examples of how to use the NativeScript dialog module."
				/>
				<Button class="btn btn-primary" text="Alert" @tap="alert" />
				<Button class="btn btn-primary" text="Confirm" @tap="confirm" />
				<Button class="btn btn-primary" text="Prompt" @tap="prompt" />
				<Button class="btn btn-primary" text="Login" @tap="login" />
				<Button class="btn btn-primary" text="Action" @tap="action" />
			</StackLayout>
		</ScrollView>
	</Page>
</template>

<script>
const { alert, confirm, prompt, login, action, inputType } = require("tns-core-modules/ui/dialogs");
export default {
  methods: {
    alert() {
      alert({
        title: "Your title",
        message: "Your message",
        okButtonText: "Your button text"
      }).then(() => {
        console.log("The user closed the alert.");
      });
    },

    confirm() {
      confirm({
        title: "Your title",
        message: "Your message",
        okButtonText: "Your button text",
        cancelButtonText: "Cancel text",
        neutralButtonText: "Neutral text"
      }).then((result) => {
        // The result property is true if the dialog is closed with the OK button, false if closed with the Cancel button or undefined if closed with a neutral button.
        console.log("Dialog result: " + result);
      });
    },

    prompt() {
      prompt({
        title: "Your title",
        message: "Your message",
        okButtonText: "Your button text",
        cancelButtonText: "Cancel text",
        neutralButtonText: "Neutral text",
        defaultText: "Default text",
        inputType: inputType.email
      }).then((result) => {
        // The result property is true if the dialog is closed with the OK button, false if closed with the Cancel button or undefined if closed with a neutral button.
        console.log("Dialog result: " + result.result);
        console.log("Text: " + result.text);
      })
    },

    login() {
      login({
        title: "Your title",
        message: "Your message",
        okButtonText: "Your button text",
        cancelButtonText: "Cancel text",
        neutralButtonText: "Neutral text",
        userName: "User name label text",
        password: "Password label text"
      }).then((result) => {
        // The result property is true if the dialog is closed with the OK button, false if closed with the Cancel button or undefined if closed with a neutral button.
        console.log("Dialog result: " + result.result);
        console.log("Username: " + result.userName);
        console.log("Password: " + result.password);
      });
    },

    action() {
      action({
        message: "Your message",
        cancelButtonText: "Cancel text",
        actions: ["Option1", "Option2"]
      }).then((result) => {
        if (result == "Option1") {
          console.log("The user selected option 1.");
        } else {
          console.log("The user selected option 2.");
        }
      });
    }
  },
};
</script>

<style scoped>
@import '~nativescript-theme-core/css/core.light.css';
.home-panel{
    font-size: 20;
    margin: 15;
}
</style>