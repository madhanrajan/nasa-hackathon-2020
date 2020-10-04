<template>
  <div id="app">
    <ImageCropper src="/snapshot4-copy.jpg" />
  </div>
</template>

<script>
import ImageCropper from "./components/ImageCropper.vue";

export default {
  name: "App",
  components: {
    ImageCropper,
  },
};
</script>

<style>
</style>
