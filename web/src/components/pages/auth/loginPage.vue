<script setup>
import AuthComponent from '../../AuthComponent.vue';
</script>

<template>
    <div>
        <AuthComponent>
            <div class="d-flex align-items-center justify-content-center border border-2 p-2 rounded-3 cardHover" style="cursor: pointer;">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-person-square" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                    <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm12 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1v-1c0-1-1-4-6-4s-6 3-6 4v1a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12z"/>
                </svg>
                <div class="ms-2 fw-bold fs-4">cool43</div>
            </div>
            <div class="text-center">
                <router-link :to="{ name: 'register' }" class="text-decoration-none" style="font-size: 14px;">ユーザーを追加</router-link>
            </div>
        </AuthComponent>
    </div>
</template>

<style>
.cardHover:hover {
    background-color: rgb(77, 77, 77);
}
</style>