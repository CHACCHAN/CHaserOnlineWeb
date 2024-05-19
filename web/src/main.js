import { createApp } from 'vue';
import { router } from './router.js';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './assets/css/style.css';

createApp(App).use(router).mount('#app');
