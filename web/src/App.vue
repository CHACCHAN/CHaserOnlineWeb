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
    <!-- {{ apple }} -->
    <router-view />
  </div>
</template>
