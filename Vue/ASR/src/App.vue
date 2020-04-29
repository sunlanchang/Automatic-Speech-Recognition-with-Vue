<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" width="10%" height="10%" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <el-divider></el-divider>
    <div class="row">
      <div class="col-md-6">
        <myaudio></myaudio>
      </div>
    </div>
    <el-divider></el-divider>
    <div class="center">
      <myAudioRecorder></myAudioRecorder>
    </div>
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import myaudio from "./components/myaudio.vue";
// 注意不要用AudioRecorder，重名编译不会报错
import myAudioRecorder from "./components/myAudioRecorder.vue";

export default {
  name: "App",
  components: {
    myaudio,
    myAudioRecorder
  },
  methods: {
    callback(msg) {
      console.debug("Event: ", msg);
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.center {
  /* margin: auto;
  width: 70%;
  border: 1px solid #73ad21;
  padding: 10px; */

  /* width: 50%;
  margin: 0 auto;
  border: 1px solid red; */

  display: table;
  margin: 0 auto;
  border: 0px solid red;
}
</style>
