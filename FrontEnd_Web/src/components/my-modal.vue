<template>
  <div class="my-modal"
    v-if="visible" @click.self="handleWrapperClick">
    <div class="my-modal__dialog">
      <header class="my-modal__header">
        <span>{{title}}</span>
        <button @click="$emit('update:visible', !visible)">Close</button>
      </header>
      <div class="my-modal__body">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'my-modal',
  props: {
    visible: {
      type: Boolean,
      require: true,
      default: false
    },
    title: {
      type: String,
      require: false,
    },
  },
  methods: {
    handleWrapperClick(){
      this.$emit('update:visible', false)
    },
  },
}
</script>

<style lang="scss">
$module: 'my-modal';
.#{$module} {
  // This is modal bg
  background-color: rgba(0,0,0,.7);
  top: 0; right: 0; bottom: 0; left: 0;
  position: fixed;
  overflow: auto;
  margin: 0;
  //This is modal layer
  &__dialog{
    left: 50%;
    top: 75px;
    width: 600px;
    position: absolute;
    background: #fff;
    margin-bottom: 50px;
  }
  &__header {
    font-size: 28px;
    font-weight: bold;
    line-height: 1.29;
    padding: 16px 16px 0 25px;
    position: relative;
  }
  &__body {
    padding: 25px;
    min-height: 150px;
    max-height: 412px;
    overflow-y: scroll;
  }
}
</style>