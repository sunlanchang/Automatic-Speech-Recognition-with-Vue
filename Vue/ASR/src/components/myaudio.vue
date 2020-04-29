<template>
  <div id="myaudio">
    <div class="large-12 cell">
      <input type="file" ref="file" v-on:change="handleChange" />
      <!-- <label for="file">Choose a file to recognize</label> -->
      <el-button v-on:click="submitUpload">Submit to recognize</el-button>
    </div>
    <div>
      <el-upload
        class="upload-demo"
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-change="handleChange"
        :file-list="fileList"
      >
        <el-button slot="trigger" size="small" type="primary">点击上传</el-button>
        <el-button
          style="margin-left: 10px;"
          size="small"
          type="success"
          v-on:click="submitUpload"
        >上传到服务器</el-button>
        <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
      </el-upload>
    </div>

    <ul>
      <li>{{class_probs['data']}}</li>
    </ul>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "myaudio",
  data: function() {
    return {
      file: "",
      class_probs: [],
      fileList: [
        {
          name: "food.jpeg",
          url:
            "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100"
        },
        {
          name: "food2.jpeg",
          url:
            "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100"
        }
      ]
    };
  },
  methods: {
    handleChange(fileList) {
      console.log("文件改变");
      // console.log(typeof fileList);
      // this.file = this.$refs.file.files[0];
      this.file = fileList;
      // this.file = fileList.slice(-3);
      console.log(this.file);
    },
    submitUpload() {
      // console.log(this.file);
      // console.log(this.fileList);
      let formData = new FormData();
      formData.append("audio", this.file);

      function getDataPromise() {
        return axios
          .post("http://localhost:5000/test", formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(function(res) {
            console.log("SUCCESS!!");
            return res.data;
          });
        // .catch(function(err) {
        //   return console.error(err);
        // });
      }
      //关键的一步！！！！！
      // https://stackoverflow.com/questions/48786445/stumped-how-do-i-get-data-in-vue-from-axios-to-display
      var self = this;
      getDataPromise().then(function(response) {
        self.class_probs = response;
        console.log("后端返回的response：", response);
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.inputfile {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}
.inputfile + label {
  font-size: 1.25em;
  font-weight: 700;
  color: white;
  /* background-color: black; */
  background-color: #c9c7c7;
  display: inline-block;
}

.inputfile:focus + label,
.inputfile + label:hover {
  background-color: rgb(55, 173, 112);
  /* background-color: white; */
}
.inputfile + label {
  cursor: pointer; /* "hand" cursor */
}
/* h3 {
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
} */
</style>
