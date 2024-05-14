<script setup>
import { onMounted } from 'vue';
import gsap from 'gsap';

onMounted(() => {
    gsap.from('.fadeIn', {
        opacity: 0,
        y: -100,
        duration: 1.5,
    });
});
</script>

<template>
    <div>
        This is Index
        <router-link :to="{ name: 'about'}">about</router-link>
        <div class="card card-body fadeIn">
            あいうえお
        </div>
    </div>
</template>