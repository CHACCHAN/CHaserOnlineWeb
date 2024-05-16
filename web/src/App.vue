<script setup>
import { ref } from 'vue';
import { router } from './router.js';
import NProgress from 'nprogress';
import 'nprogress/nprogress.css';

const pageRouteFlag = ref(false);

NProgress.configure({
  showSpinner: false,
});

router.beforeEach((to, from, next) => {
  pageRouteFlag.value = true;
  NProgress.start();
  next();
});

router.afterEach(() => {
  setTimeout(() => {
    NProgress.done();
    pageRouteFlag.value = false;
  }, 100);
});

</script>


<!-- <script setup>
import { ref, onMounted } from 'vue';
import CHaserOnlineController from './assets/js/CHaserOnlineClient';

const apple = ref();
onMounted(() => {
  CHaserOnlineClient()
});

const CHaserOnlineClient = async () => {
  let flag = false;
  const CHaserOnlineClient = new CHaserOnlineController({
    url : 'http://www7019ug.sakura.ne.jp/CHaserOnline003/user/',
    user : 'cool46',
    password: 'cool',
    room: 6081,
  });

  const connectStatus = await CHaserOnlineClient.connect();
  if(connectStatus.status === 'bad')
    console.log('error');
  while(!flag && connectStatus.status === 'ok') {
    apple.value = await CHaserOnlineClient.getready();
    apple.value = await CHaserOnlineClient.action();
    flag = await CHaserOnlineClient.gameSet();
    if(flag) console.log('gameSet');
    console.log('while' + flag);
  }
}
</script> -->


<template>
  <div>
    <div class="position-fixed top-0 left-0 z-3" style="width: 100%; height: 100vh;" v-if="pageRouteFlag"></div>
    <!-- {{ apple }} -->
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