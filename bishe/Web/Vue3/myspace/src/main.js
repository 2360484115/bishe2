import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import locale from 'element-plus/es/locale/lang/zh-cn';
import Cookies from 'js-cookie'
import 'font-awesome/css/font-awesome.min.css';
//import '@fortawesome/fontawesome-free/css/all.min.css';

const app = createApp(App);

createApp(App).use(store).use(router).mount('#app')

app.use(ElementPlus, {
    locale: locale,
    // 支持 large、default、small
    size: Cookies.get('size') || 'default'
  })