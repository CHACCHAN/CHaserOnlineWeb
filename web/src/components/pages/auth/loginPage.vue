<script setup>
import AuthComponent from '../../AuthComponent.vue';
</script>

<template>
    <div>
        <AuthComponent :title="'❚ ログインする'">
            <div class="d-flex align-items-center justify-content-center border border-2 border-secondary p-2 rounded-3 cardHover mb-2" style="cursor: pointer;">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
                <div class="ms-2 fs-4">cool43</div>
            </div>
            <router-link :to="{ name: 'register' }" class="btn btn-success py-1 fw-bold w-100" style="font-size: 14px;">Add User</router-link>
        </AuthComponent>
    </div>
</template>

<style>
.cardHover:hover {
    background-color: rgb(77, 77, 77);
}
</style>