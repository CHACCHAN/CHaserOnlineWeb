<script setup>
import { ref, onMounted } from 'vue';
import AuthComponent from '../../AuthComponent.vue';

const users = ref(null);
const getUser_cashKey = ref('get_user');

const getUser = async() => {
    const cashData = JSON.parse(localStorage.getItem(getUser_cashKey.value));
    if(cashData) { 
        users.value = cashData;
        // return; 新規登録ユーザ更新用
    }

    await fetch('http://localhost:8080/api/get_user')
    .then((response) => response.json())
    .then((res) => { users.value = res });
    localStorage.setItem(getUser_cashKey.value, JSON.stringify(users.value));
}
// const login = async() => {
//     await fetch('http://localhost:8080/api/signin', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({
//             username: 'cool',
//             password: 'cool',
//         })
//     })
// }

onMounted(() => {
    getUser();
});
</script>

<template>
    <div>
        <AuthComponent :title="'❚ ログインする'">
            <div class="d-flex align-items-center justify-content-center" v-if="!users">
                <div class="spinner-border" role="status"></div>
                <div class="ms-2 fw-bold">Loading</div>
            </div>
            <div class="d-flex align-items-center justify-content-start border border-2 border-secondary p-2 rounded-3 cardHover mb-2" style="cursor: pointer;" v-for="user in users" :key="user">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
                <div class="ms-2 fs-4">{{ user.username }}</div>
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