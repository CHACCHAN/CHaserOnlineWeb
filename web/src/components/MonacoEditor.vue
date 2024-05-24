<script setup>
import { ref, onMounted, onBeforeUnmount, defineProps, defineEmits } from 'vue';
import loader from '@monaco-editor/loader';

const props = defineProps({
    value: String,
    language: String,
});
const emit = defineEmits(['getValue']);
const editorContainer = ref(null);
let editor;

onMounted(() => {
    loader.init().then((monaco) => {
        editor = monaco.editor.create(editorContainer.value, {
            value: props.value,
            language: props.language,
            theme: 'vs-dark',
            automaticLayout: true,
        });
        editor.onDidChangeModelContent(() => {
            emit('getValue', editor.getValue());
        });
    });
});

onBeforeUnmount(() => {
    if(editor) editor.dispose();
});
</script>

<template>
    <div ref="editorContainer" class="editor-container"></div>
</template>

<style>
.editor-container {
    width: 100%;
    height: 100vh;
}
</style>
  