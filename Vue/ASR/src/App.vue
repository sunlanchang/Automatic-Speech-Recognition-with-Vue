<template>
  <div id="app">
    <el-container>
      <el-header>
        <navigator></navigator>
      </el-header>
      <el-main>
        <img alt="Vue logo" src="./assets/logo.png" width="10%" height="10%" />
        <!-- <el-divider></el-divider> -->
        <el-row>
          <el-col :span="8">
            <div class="grid-content"></div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content">
              <myaudio></myaudio>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content"></div>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <div class="center">
          <myAudioRecorder></myAudioRecorder>
        </div>
      </el-main>
      <el-footer></el-footer>
    </el-container>
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import myaudio from "./components/myaudio.vue";
// 注意不要用AudioRecorder，重名编译不会报错
import myAudioRecorder from "./components/myAudioRecorder.vue";
import navigator from "./components/navigator.vue";

export default {
  name: "App",
  components: {
    myaudio,
    myAudioRecorder,
    navigator
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
  display: table;
  margin: 0 auto;
  border: 0px solid red;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
