<script setup>
import { onMounted, ref } from 'vue';
import CHaserOnlineController from './assets/js/CHaserOnlineClient';

const apple = ref();
const flag = ref(false)

onMounted(() => {
  CHaserOnlineClient()
});

const CHaserOnlineClient = async () => {
  const CHaserOnlineClient = new CHaserOnlineController({
    url : 'http://www7019ug.sakura.ne.jp/CHaserOnline003/user/',
    user : 'cool44',
    password: 'cool',
    room: 6094,
  });

  await CHaserOnlineClient.connect();
  while(!flag.value) {
    apple.value = await CHaserOnlineClient.getready();
    apple.value = await CHaserOnlineClient.action();
    flag.value = await CHaserOnlineClient.gameSet();
    console.log('while' + flag.value);
  }
}
</script>


<template>
  <div>
    {{ apple }}
  </div>
</template>
