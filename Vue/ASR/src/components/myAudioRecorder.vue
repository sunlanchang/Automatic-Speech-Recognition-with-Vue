<style lang="scss">
.toggle {
  cursor: pointer;
  margin: 20px;
}
</style>

<template>
  <div class="row" id="test">
    <!-- <div class="toggle" @click="toggle">TOGGLE</div> -->

    <audio-recorder
      v-if="showRecorder"
      upload-url="http://localhost:5000/test"
      filename="ninja"
      format="wav"
      :attempts="3"
      :time="2"
      :headers="headers"
      :before-recording="callback"
      :pause-recording="callback"
      :after-recording="callback"
      :select-record="callback"
      :before-upload="callback"
      :successful-upload="mycallback"
      :failed-upload="callback"
      :bit-rate="192"
    />

    <el-input
      :disabled="true"
      type="textarea"
      autosize
      placeholder="这里显示语音识别结果..."
      v-model="response_en_sentence"
    ></el-input>
    <el-input
      :disabled="true"
      type="textarea"
      autosize
      placeholder="这里显示翻译结果..."
      v-model="response_zh_sentence"
    ></el-input>
  </div>
</template>

<script>
export default {
  name: "myAudioRecorder",
  data() {
    return {
      mp3: "/demo/example.mp3",
      showRecorder: true,
      headers: {
        "X-Custom-Header": "some data"
      },
      response_en_sentence: "",
      response_zh_sentence: ""
    };
  },
  methods: {
    callback(msg) {
      console.log("Event: ", msg);
    },
    mycallback(res) {
      // console.log("Event: ", res);
      this.response_en_sentence = res["data"]["en_sentence"];
      this.response_zh_sentence = res["data"]["zh_sentence"];
    },
    toggle() {
      this.showRecorder = !this.showRecorder;
    }
  }
};
</script>