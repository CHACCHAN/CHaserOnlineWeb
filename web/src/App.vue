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
    user : 'cool44',
    password: 'cool',
    room: 6094,
  });

  await CHaserOnlineClient.connect();
  while(!flag) {
    apple.value = await CHaserOnlineClient.getready();
    apple.value = await CHaserOnlineClient.action();
    flag = await CHaserOnlineClient.gameSet();
    console.log('while' + flag);
  }
}
</script> -->


<template>
  <div>
    <!-- {{ apple }} -->
    <router-view />
  </div>
</template>
