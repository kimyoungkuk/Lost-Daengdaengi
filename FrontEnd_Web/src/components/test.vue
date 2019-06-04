<template>
  <div class="backgroundImage" v-bind:style="{ 'background-image': 'url(' + img1 + ')'}">
    <link href="https://fonts.googleapis.com/css?family=Jua&display=swap&subset=korean" rel="stylesheet">
    <h1 class="googleFont">1. 제목을 입력하세요.</h1>
    <b-form @submit="onClick">
      <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="title"
          required
          placeholder="Enter name"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" router-link to='/finderForm2'>Submit</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        img1: require('../assets/formBackgroundImg.jpg'),
        title: ''
      }
    },
    methods: {
      onClick(evt) {
        evt.preventDefault()
        this.$store.state.FinderPost.title = this.title;
        console.log(this.$store.state.FinderPost.title);
      }
      // onSubmit(evt) {
      //   evt.preventDefault()
      //   alert(JSON.stringify(this.form))
      // },
      // onReset(evt) {
      //   evt.preventDefault()
      //   // Reset our form values
      //   this.form.email = ''
      //   this.form.name = ''
      //   this.form.food = null
      //   this.form.checked = []
      //   // Trick to reset/clear native browser form validation state
      //   this.show = false
      //   this.$nextTick(() => {
      //     this.show = true
      //   })
      // }
    }
  }
</script>

<style>
.backgroundImage {
    width: 100%;
    height: 100%;
    position: absolute;
    background-size: cover;
    background-position: center;
    top: 0;
    left: 0;
    }
.googleFont {
    font-family: 'Jua', sans-serif;
    color:cornsilk;
}
</style>