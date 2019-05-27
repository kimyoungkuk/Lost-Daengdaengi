<template>
  <div>
          <div>
    <b-progress :value="counter" :max="max" show-progress animated></b-progress>
    <b-progress class="mt-2" :max="max" show-value>
      <b-progress-bar :value="counter*(6/10)" variant="success"></b-progress-bar>
      <b-progress-bar :value="counter*(2.5/10)" variant="warning"></b-progress-bar>
      <b-progress-bar :value="counter*(1.5/10)" variant="danger"></b-progress-bar>
    </b-progress>
    <b-button class="mt-3" @click="clicked">Click me</b-button>
  </div>
  <template>
  <div>
    <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
    <div class="mt-2">Value: {{ text }}</div>
  </div>
</template>
<template>
  <b-container fluid>
    <b-row class="my-1" v-for="type in types" :key="type">
      <b-col sm="3">
        <label :for="`type-${type}`">Type {{ type }}:</label>
      </b-col>
      <b-col sm="9">
        <b-form-input :id="`type-${type}`" :type="type"></b-form-input>
      </b-col>
    </b-row>
  </b-container>
</template>



  </div>
</template>

<script>
export default {
 data() {
      return {
        text: '',
        slide: 0,
        sliding: null,
        counter: 45,
        max: 100,
        types: [
          'text',
          'password',
          'email',
          'number',
          'url',
          'tel',
          'date',
          `time`,
          'range',
          'color'
        ]
      }
    },
    methods: {
      clicked() {
        this.counter = Math.random() * this.max
        console.log('Change progress to ' + Math.round(this.counter * 100) / 100)
      },
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
