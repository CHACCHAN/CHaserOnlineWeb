<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import gsap from 'gsap';
import Cookies from 'js-cookie';

const router = useRouter();
const fetchAPI = ref(null);
const viewFlag = ref(false);
const status = ref(null);

const checkUser = async() => {
    const jwt_token = Cookies.get('jwt_token');
    await fetch('http://localhost:8080/api/protected', {
        headers: { Authorization: `Bearer ${jwt_token}` }
    })
    .then((response) => response.json())
    .then((res) => {
        fetchAPI.value = res;
        if(!res.status === 'ok' || res.status === undefined )
            router.push({ name: 'login' });
        else {
            viewFlag.value = true;
            status.value = {status: 'ok', message: 'ログインしました'};
        }
    });
}

onMounted(() => {
    checkUser();
    gsap.from('.fadeIn', {
        opacity: 0,
        y: -100,
        delay: .5,
        duration: 1.5,
    });
});
</script>

<template>
    <div class="backgroundDarkBlue" style="height: 100vh;">
        <div v-if="viewFlag">
            <header class="text-light px-3 d-flex align-items-center justify-content-start">
                <img src="../../assets/image/CHaserOnline.jpg" width="30" height="30" class="rounded-circle" />
                <div class="fs-4 ms-2">CHaserOnline Web</div>
            </header>
            <div class="p-3">
                <div class="row">
                    <!-- マップ要素 -->
                    <div class="col-12 col-md-7 mb-1">
                        <div class="text-success fw-bold d-flex align-items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cpu" viewBox="0 0 16 16">
                                <path d="M5 0a.5.5 0 0 1 .5.5V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2A2.5 2.5 0 0 1 14 4.5h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14a2.5 2.5 0 0 1-2.5 2.5v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14A2.5 2.5 0 0 1 2 11.5H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2A2.5 2.5 0 0 1 4.5 2V.5A.5.5 0 0 1 5 0zm-.5 3A1.5 1.5 0 0 0 3 4.5v7A1.5 1.5 0 0 0 4.5 13h7a1.5 1.5 0 0 0 1.5-1.5v-7A1.5 1.5 0 0 0 11.5 3h-7zM5 6.5A1.5 1.5 0 0 1 6.5 5h3A1.5 1.5 0 0 1 11 6.5v3A1.5 1.5 0 0 1 9.5 11h-3A1.5 1.5 0 0 1 5 9.5v-3zM6.5 6a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3z"/>
                            </svg>
                            <div class="ms-1">マップレンダリング</div>
                        </div>
                        <div class="border border-success rounded-bottom text-light">
                            ss <br>
                            ss <br>
                            sss
                        </div>
                        <div class="text-start mt-1">
                            <button class="btn btn-success p-1 py-0">実行</button>
                        </div>
                    </div>
                    <!-- サブ要素 -->
                    <div class="col-12 col-md-5">
                        <div class="row">
                            <div class="col-12 mb-1">
                                <!-- コマンド -->
                                <div class="text-light fw-bold d-flex align-items-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-terminal" viewBox="0 0 16 16">
                                        <path d="M6 9a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3A.5.5 0 0 1 6 9zM3.854 4.146a.5.5 0 1 0-.708.708L4.793 6.5 3.146 8.146a.5.5 0 1 0 .708.708l2-2a.5.5 0 0 0 0-.708l-2-2z"/>
                                        <path d="M2 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H2zm12 1a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h12z"/>
                                    </svg>
                                    <div class="ms-1">実行コマンド</div>
                                </div>
                                <div class="border border-light rounded-bottom text-light p-3 overflow-auto" style="height: 400px;">
                                    <div class="card card-body p-1 text-bg-dark mb-1">
                                        <div class="text-danger fw-bold">GetReady</div>
                                        <div class="text-light">command1=gr, returnCode=[50, 50, 40, 60, 1000, 60, 85, 65, 44, 22]</div>
                                    </div>
                                    <div class="card card-body p-1 text-bg-dark mb-1">
                                        <div class="text-success fw-bold">Action</div>
                                        <div class="text-light">command2=wu, returnCode=[50, 50, 40, 60, 1000, 60, 85, 65, 44, 22]</div>
                                    </div>
                                    <div class="card card-body p-1 text-bg-dark mb-1">
                                        <div class="text-warning fw-bold">Complete✓</div>
                                        <div class="text-light">command3=#, returnCode=[50, 50, 40, 60, 1000, 60, 85, 65, 44, 22]</div>
                                    </div>
                                    <div class="card card-body p-1 text-bg-dark mb-1">
                                        <div class="text-danger fw-bold">GetReady</div>
                                        <div class="text-light">command1=gr, returnCode=[50, 50, 40, 60, 1000, 60, 85, 65, 44, 22]</div>
                                    </div>
                                    <div class="card card-body p-1 text-bg-dark mb-1">
                                        <div class="text-success fw-bold">Action</div>
                                        <div class="text-light">command2=wu, returnCode=[50, 50, 40, 60, 1000, 60, 85, 65, 44, 22]</div>
                                    </div>
                                    <div class="card card-body p-1 text-bg-dark mb-1">
                                        <div class="text-warning fw-bold">Complete✓</div>
                                        <div class="text-light">command3=#, returnCode=[50, 50, 40, 60, 1000, 60, 85, 65, 44, 22]</div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <!-- コントロール -->
                                <div class="text-light fw-bold d-flex align-items-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chat-dots" viewBox="0 0 16 16">
                                        <path d="M5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                                        <path d="m2.165 15.803.02-.004c1.83-.363 2.948-.842 3.468-1.105A9.06 9.06 0 0 0 8 15c4.418 0 8-3.134 8-7s-3.582-7-8-7-8 3.134-8 7c0 1.76.743 3.37 1.97 4.6a10.437 10.437 0 0 1-.524 2.318l-.003.011a10.722 10.722 0 0 1-.244.637c-.079.186.074.394.273.362a21.673 21.673 0 0 0 .693-.125zm.8-3.108a1 1 0 0 0-.287-.801C1.618 10.83 1 9.468 1 8c0-3.192 3.004-6 7-6s7 2.808 7 6c0 3.193-3.004 6-7 6a8.06 8.06 0 0 1-2.088-.272 1 1 0 0 0-.711.074c-.387.196-1.24.57-2.634.893a10.97 10.97 0 0 0 .398-2z"/>
                                    </svg>
                                    <div class="ms-1">メッセージ</div>
                                </div>
                                <div class="border border-light rounded-bottom text-light p-3">
                                    <div class="mb-1">
                                        <div class="text-primary">ステータス</div>
                                        <div class="text-bg-success rounded" v-if="status?.status === 'ok'">> {{ status?.message }}</div>
                                        <div class="text-bg-danger rounded" v-else-if="status?.status === 'bad'">> {{ status?.message }}</div>
                                    </div>
                                    <div class="text-primary">Fetch API</div>
                                    <div v-text="fetchAPI"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>