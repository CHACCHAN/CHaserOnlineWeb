<script setup>
import { onMounted, ref } from 'vue';
import { router } from './router.js';
import NProgress from 'nprogress';
import 'nprogress/nprogress.css';
// import CHaserOnlineController from './assets/js/CHaserOnlineClient';

const pageRouteFlag = ref(false);
// const apple = ref();

NProgress.configure({
  showSpinner: false,
});

router.beforeEach((to, from, next) => {
  pageRouteFlag.value = true;
  NProgress.start();
  next();
});

router.afterEach(() => {
  NProgress.done();
  pageRouteFlag.value = false;
});

window.addEventListener('beforeunload', () => {
  localStorage.clear();
});

// const CHaserOnlineClient = async () => {
//   let flag = false;
//   const CHaserOnlineClient = new CHaserOnlineController({
//     url : 'http://www7019ug.sakura.ne.jp/CHaserOnline003/user/',
//     user : 'cool47',
//     password: 'cool',
//     room: 6082,
//   });

//   const connectStatus = await CHaserOnlineClient.connect();
//   if(connectStatus.status === 'bad')
//     console.log('error');
//   while(!flag && connectStatus.status === 'ok') {
//     apple.value = await CHaserOnlineClient.getready();
//     apple.value = await CHaserOnlineClient.action();
//     flag = await CHaserOnlineClient.gameSet();
//     if(flag) console.log('gameSet');
//     console.log('while' + flag);
//   }
// }

onMounted(() => {
});
</script>


<template>
  <div>
    <div class="position-fixed top-0 left-0 z-3" style="width: 100%; height: 100vh;" v-if="pageRouteFlag"></div>
    <!-- {{ apple }} -->
    <!-- <button @click="CHaserOnlineClient()">実行</button> -->
    <router-view />
  </div>
</template>

<style>
#nprogress .bar {
  background: -moz-linear-gradient(left, #3cff00, #00ff73);
  background: -webkit-linear-gradient(left, #3cff00, #00ff73);
  background: linear-gradient(to right, #3cff00, #00ff73);
  box-shadow: 0 0 10px #3cff00;
}
</style>