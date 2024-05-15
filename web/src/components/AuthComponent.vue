<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    title: String,
});
</script>

<template>
    <div class="position-relative">
        <img src="https://i.ytimg.com/vi/e_yU9oO5ay0/maxresdefault.jpg" class="overCanvas" style="" />
        <div class="position-absolute top-0 left-0 w-100">
            <div class="d-flex align-items-center justify-content-center" style="width: 100%; height: 100vh;">
                <div>
                    <div class="text-success fw-bold" style="font-size: 14px;">{{ props.title }}</div>
                    <div class="card border-0 text-light backgroundDarkBlue rounded-0 border-top border-3 border-success shadow-lg">
                        <div class="card-body">
                            <slot />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.overCanvas {
    width: 100%;
    height: 100vh;
    filter: brightness(30%);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
    object-fit: cover;
}
</style>