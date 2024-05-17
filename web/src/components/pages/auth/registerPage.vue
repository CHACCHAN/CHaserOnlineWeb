<script setup>
import { ref } from 'vue';
import AuthComponent from '../../AuthComponent.vue';

const inputUser = ref();
const inputPass = ref();

const submitForm = async() => {
    await fetch('http://localhost:8080/api/require', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            username: inputUser.value,
            password: inputPass.value,
        })
    })
    .then((response) => response.json())
    .then((res) => {
        console.log(res)
    });
}
</script>

<template>
    <div>
        <AuthComponent :title="'❚ ユーザー登録'">
            <label for="inputUser">Username</label>
            <input type="text" id="inputUser" v-model="inputUser" class="form-control text-bg-dark border-0 p-1 px-2 mb-1" />
            <label for="inputPass">Password</label>
            <input type="text" id="inputPass" v-model="inputPass" class="form-control text-bg-dark border-0 p-1 px-2 mb-3" />
            <button class="btn btn-success py-1 fw-bold w-100" @click="submitForm()" :disabled="!inputUser || !inputPass">Submit</button>
            <router-link :to="{ name: 'login' }" class="btn text-light py-1 fw-bold border-0 w-100">Chancel</router-link>
        </AuthComponent>
    </div>
</template>