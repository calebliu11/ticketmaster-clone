import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'http://3.12.34.169'

createApp(App).use(store).use(router, axios).mount('#app')
