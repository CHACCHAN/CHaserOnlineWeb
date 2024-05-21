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
  NProgress.done();
  pageRouteFlag.value = false;
});

window.addEventListener('beforeunload', () => {
  localStorage.clear();
});
</script>


<template>
  <div>
    <div class="position-fixed top-0 left-0 z-3" style="width: 100%; height: 100vh;" v-if="pageRouteFlag"></div>
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