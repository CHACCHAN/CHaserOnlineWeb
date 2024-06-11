<script setup>
import { onMounted } from 'vue';
import MonacoEditor from '../MonacoEditor.vue';

const getValueEmit = (newData) => {
    console.log('data' + newData);
}

onMounted(() => {
    document.title = 'Editor';
    document.querySelector('body').classList.add('overflow-hidden');
})
</script>

<template>
    <div class="row overflow-hidden">
        <div class="col-12 col-md-2">
            <div class="text-danger">開発途中につき、ご利用いただけません</div>
            <div class="text-danger">ここでは、クライアントの動作コードを入力するためのWebコードエディタになります</div>
        </div>
        <div class="col-12 col-md-10">
            <MonacoEditor 
                language="javascript"
                value=
"// JavaScript プレビュー例
var ActionReturnNumber = [10, 78, 11, 22, 1000, 10, 12, 32, 44];
var GetReadyMode = 4;
var param = '';

if(ActionReturnNumber[1] >= 70 && ActionReturnNumber[1] <= 79) {
    GetReadyMode = 1;
} else if(ActionReturnNumber[3] >= 70 && ActionReturnNumber[3] <= 79) {
    GetReadyMode = 3;
} else if(ActionReturnNumber[5] >= 70 && ActionReturnNumber[5] <= 79) {
    GetReadyMode = 5;
} else if(ActionReturnNumber[7] >= 70 && ActionReturnNumber[7] <= 79) {
    GetReadyMode = 7;
} else {
    GetReadyMode = 4;
}
switch(GetReadyMode) {
    case 1:
        param = 'gru';
        break;
    case 3:
        param = 'grl';
        break;
    case 5:
        param = 'grr';
        break;
    case 7:
        param = 'grd';
        break;
    default:
        param = 'gr';
}"
                @getValue="getValueEmit"
            />
        </div>
    </div>
</template>