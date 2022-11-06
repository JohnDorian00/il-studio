import { createApp } from 'vue'
import App from './App.vue'
import mitt from 'mitt';

const emitter = mitt();

const app = createApp(App)
app.config.globalProperties.emitter = emitter;
app.config.globalProperties.backendIp = "192.168.1.236"
app.mount('#app');
