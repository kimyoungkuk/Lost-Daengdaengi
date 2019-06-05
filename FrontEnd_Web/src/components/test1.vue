<template>
  <div>
    <div v-bind:class="[show ? blurClass : '', backClass]">
      <h1>Transition Demo</h1>
    </div>
    <b-button @click="show = !show">
      Toggle
    </b-button>
    <transition name="fade">
      <div v-if="show">
        <h1>{{demo}}</h1>
      </div>
    </transition>
  </div>  
</template>

<script>
export default {
  data () {
    return {
      demo: 'Transition Me',
      show: false,
      backClass: 'bk',
      blurClass: 'blur'
    }
  }
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 2.5s ease-out;
   
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.bk {
  transition: all 0.1s ease-out;
}

.blur {
  filter: blur(2px);
  opacity: 0.4;
}
</style>
