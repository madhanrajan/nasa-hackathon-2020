<template>
  <div class="">
    <div class="img-container">
      <img ref="image" :src="src" />
      <img :src="destination" class="img-preview" />
      <button class="submit-button" v-on:click="click">Classify</button>
      <p>{{ returnText }}</p>
    </div>
  </div>
</template>

<script>
import Cropper from "cropperjs";
import $ from "jquery";

export default {
  name: "ImageCropper",
  props: {
    src: String,
  },
  methods: {
    click: function (event) {
      var me = this;
      me.returnText = "Please wait";
      this.cropper
        .getCroppedCanvas({
          minWidth: 256,
          minHeight: 256,
          maxWidth: 4096,
          maxHeight: 4096,
          fillColor: "#fff",
          imageSmoothingEnabled: true,
          imageSmoothingQuality: "high",
        })
        .toBlob(function (blob) {
          let file = new File([blob], "test.jpeg");
          const formData = new FormData();
          formData.append("image", file);
          formData.append("Content-Type", "multipart/form-data");
          $.ajax({
            method: "POST",
            url: "http://localhost:8000/upload",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
          })
            .done(function (data) {
              console.log(data);
              me.returnText = data;
            })
            .fail(function (err) {
              console.log(err);
            });
        });
      // formData.append("image", this.destination);

      if (event) {
        event.target.tagName;
      }
    },
  },

  data() {
    return {
      cropper: {},
      destination: {},
      image: {},
      returnText:
        "Welcome to the state of the art cloud classifier, Choose image to clasify",
    };
  },

  mounted() {
    this.image = this.$refs.image;
    this.cropper = new Cropper(this.image, {
      zoomable: true,
      scalable: false,
      aspectRatio: 1,
      crop: () => {
        const canvas = this.cropper.getCroppedCanvas();
        this.destination = canvas.toDataURL("image/jpeg");
      },
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img-container {
  width: 1200px;
  height: 600px;
}

.img-preview {
  width: 100px;
  height: 100px;
  margin-top: 5px;
}
.submit-button {
  margin-left: 50px;
}
p {
  margin-top: -5px;
}
</style>
