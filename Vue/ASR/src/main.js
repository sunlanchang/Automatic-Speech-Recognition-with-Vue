import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import AudioRecorder from 'vue-audio-recorder'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);
Vue.use(AudioRecorder)
Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  render: h => h(App),
}).$mount('#app')
