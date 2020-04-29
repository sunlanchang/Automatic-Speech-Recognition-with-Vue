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
    <!-- <audio-recorder
      upload-url="YOUR_API_URL"
      :attempts="3"
      :time="2"
      :before-recording="callback"
      :pause-recording="callback"
      :after-recording="callback"
      :select-record="callback"
      :before-upload="callback"
      :successful-upload="callback"
      :failed-upload="callback"
    />-->
    <!-- <audio-player :src="mp3" v-if="!showRecorder" /> -->
    <ul>
      <li>{{sentence}}</li>
    </ul>
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
      sentence: ""
    };
  },
  methods: {
    callback(msg) {
      console.log("Event: ", msg);
    },
    mycallback(res) {
      // console.log("Event: ", res);
      this.sentence = res["data"]["data"];
    },
    toggle() {
      this.showRecorder = !this.showRecorder;
    }
  }
};
</script>