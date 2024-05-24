<script setup>
import { onMounted } from 'vue';
import MonacoEditor from '../MonacoEditor.vue';

const getValueEmit = (newData) => {
    console.log('data' + newData);
}

onMounted(() => {
    document.querySelector('body').classList.add('overflow-hidden');
})
</script>

<template>
    <div class="row overflow-hidden">
        <div class="col-12 col-md-2">
            <router-link :to="{ name: 'dashboard' }">戻る</router-link>
        </div>
        <div class="col-12 col-md-10">
            <MonacoEditor 
                language="javascript"
                value="// Type your code here..."
                @getValue="getValueEmit"
            />
        </div>
    </div>
</template>