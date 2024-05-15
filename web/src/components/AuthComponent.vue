<template>
    <div class="position-relative">
        <img src="https://i.ytimg.com/vi/e_yU9oO5ay0/maxresdefault.jpg" class="overCanvas" />
        <div class="position-absolute top-0 left-0 w-100">
            <div class="d-flex align-items-center justify-content-center" style="width: 100%; height: 100vh;">
                <div class="card border-0 text-light backgroundDarkBlue">
                    <div class="card-body">
                        <slot />
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