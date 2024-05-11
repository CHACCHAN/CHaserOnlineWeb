<script setup>
import { onMounted, ref } from 'vue';

const apple = ref();

onMounted(() => {
  fetch('http://localhost:8080/api/fuck')
  .then((response) => response.json())
  .then((res) => apple.value = res);
});
</script>


<template>
  <div>
    {{ apple?.test }}
  </div>
</template>
