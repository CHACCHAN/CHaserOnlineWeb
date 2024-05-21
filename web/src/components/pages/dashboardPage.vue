<script setup>
import { onMounted, onUpdated, ref } from 'vue';
import { useRouter } from 'vue-router';
import Cookies from 'js-cookie';
import CHaserOnlineController from '../../assets/js/CHaserOnlineClient.js';

const router = useRouter();
const fetchAPI = ref(null);
const viewFlag = ref(false);
const settingSendFlag = ref(false);
const status = ref(null);
const users = ref(null);
const username = ref();
const password = ref();
const roomNumber = ref('');
const CHaserOnlineServerURL = ref(null);
const CHaserOnlineProxy = ref(null);

const getUser = async() => {
    await fetch('http://localhost:8080/api/get_user')
    .then((response) => response.json())
    .then((res) => { 
        users.value = res;
    });
}
const checkUser = async() => {
    const jwt_token = Cookies.get('jwt_token');
    await fetch('http://localhost:8080/api/protected', {
        headers: { Authorization: `Bearer ${jwt_token}` }
    })
    .then((response) => response.json())
    .then((res) => {
        fetchAPI.value = res;
        if(!res?.status === 'ok' || res?.status === undefined )
            router.push({ name: 'login' });
        else {
            viewFlag.value = true;
            username.value = res.username;
            password.value = res.password;
            status.value = {status: 'ok', message: 'ログインしました'};
        }
    });
}
const deleteUser = async(user_id) => {
    const jwt_token = Cookies.get('jwt_token');
    await fetch('http://localhost:8080/api/remove', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json',
            Authorization: `Bearer ${jwt_token}`
        },
        body: JSON.stringify({
            user_id: user_id,
        })
    })
    .then((response) => response.json())
    .then((res) => {
        if(res?.status === 'ok') {
            fetchAPI.value = res;
            status.value = {status: 'ok', message: '正常にユーザを削除しました'};
            getUser();
        } else {
            fetchAPI.value = res;
        }
    });
}
const onMousemove = (type, index) => {
    if(type === 'enter')
        document.getElementById(index + 'trash').classList.remove('d-none');
    else
        document.getElementById(index + 'trash').classList.add('d-none');
}
const sendSetting = async() => {
    settingSendFlag.value = true;
    const jwt_token = Cookies.get('jwt_token');
    await fetch('http://localhost:8080/api/chaseronline/post/setting', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json',
            Authorization: `Bearer ${jwt_token}`
        },
        body: JSON.stringify({
            CHaserOnlineServerURL: CHaserOnlineServerURL.value,
            CHaserOnlineProxy: CHaserOnlineProxy.value
        })
    })
    .then((response) => response.json())
    .then((res) => {
        fetchAPI.value = res;
        settingSendFlag.value = false;
        if(res?.status === 'ok') {
            status.value = {status: 'ok', message: '正常に設定を更新しました'};
        } else {
            status.value = {status: 'bad', message: 'エラー:' + ' ' + res.message};
        }
        
        getSetting();
    });
}
const getSetting = async() => {
    const jwt_token = Cookies.get('jwt_token');
    await fetch('http://localhost:8080/api/chaseronline/get/setting', {
        headers: { Authorization: `Bearer ${jwt_token}` }
    })
    .then((response) => response.json())
    .then((res) => {
        if(res?.status) {
            fetchAPI.value = res;
            CHaserOnlineServerURL.value = res.data.CHaserOnlineServerURL;
            CHaserOnlineProxy.value = res.data.CHaserOnlineProxy;
        } else {
            fetchAPI.value = res;
        }
    });
}
const CHaserOnlineClient = async () => {
    let flag = false;
    const CHaserOnlineClient = new CHaserOnlineController({
        url: CHaserOnlineServerURL.value,
        proxy: CHaserOnlineProxy.value,
        user: username.value,
        password: password.value,
        room: roomNumber.value,
    });

    const connectStatus = await CHaserOnlineClient.connect();
    if(connectStatus.status === 'bad')
        console.log('error');
    while(!flag && connectStatus.status === 'ok') {
        await CHaserOnlineClient.getready();
        await CHaserOnlineClient.action();
        flag = await CHaserOnlineClient.gameSet();
        if(flag) console.log('gameSet');
        console.log('while' + flag);
    }
}

onMounted(async() => {
    await checkUser();
    await getSetting();
    await getUser();
});

onUpdated(async() => {
    await checkUser()
});
</script>

<template>
    <div class="backgroundDarkBlue" style="height: 100vh;">
        <Transition>
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
                            <div class="border border-success rounded-bottom text-light mb-2">
                                ss <br>
                                ss <br>
                                sss
                            </div>
                            <div class="card card-body text-bg-dark">
                                <div class="row">
                                    <div class="col-6 col-md-3">
                                        <label for="inputRoom" class="d-flex align-items-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
                                                <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
                                            </svg>
                                            <div class="ms-1">ルーム番号</div>
                                        </label>
                                        <div class="border border-secondary rounded">
                                            <input type="number" v-model="roomNumber" id="inputRoom" class="border-0 rounded-top border-bottom border-secondary py-1 text-bg-dark w-100" />
                                            <button class="btn btn-dark rounded-0 text-light col-4" v-for="number in 9" :key="number" @click="roomNumber += number.toString()">
                                                <div>{{ number }}</div>
                                            </button>
                                            <button class="btn border-0 text-light col-4" v-for="command in ['', '0', 'C']" :key="command">
                                                <div class="text-light" v-if="command == '0'" @click="roomNumber += command.toString()">{{ command }}</div>
                                                <div class="text-danger" v-else @click="roomNumber = ''">{{ command }}</div>
                                            </button>
                                        </div>
                                    </div>
                                    <div class="col-6 col-md-3">
                                        <div class="d-flex align-items-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
                                                <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
                                            </svg>
                                            <div class="ms-1">ログイン中</div>
                                        </div>
                                        <div class="border border-secondary rounded p-1 d-flex align-items-center text-truncate mb-2">
                                            <div class="text-secondary">username :</div>
                                            <div class="text-light ms-1">{{ username }}</div>
                                        </div>
                                        <div class="d-flex align-items-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
                                                <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
                                            </svg>
                                            <div class="ms-1">他ユーザ</div>
                                        </div>
                                        <div class="border border-secondary rounded p-1 text-truncate">
                                            <div v-for="(user, index) in users" :key="user" class="text-light">
                                                <div class="d-flex align-items-center" v-if="user.username != username" @mouseleave="onMousemove('leave', index)">
                                                    <svg 
                                                        :id="index + 'trash'" 
                                                        xmlns="http://www.w3.org/2000/svg" 
                                                        width="16" height="16" fill="currentColor" 
                                                        class="bi bi-trash3 me-1 d-none text-danger" 
                                                        viewBox="0 0 16 16" style="cursor: pointer;"
                                                        @click="deleteUser(user.user_id)"
                                                    >
                                                        <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z"/>
                                                    </svg>
                                                    <div @mouseenter="onMousemove('enter', index)">{{ user.username }}</div>
                                                </div>
                                            </div>
                                            <div v-if="!users || !users[1]">NULL</div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6">
                                        <div class="d-flex align-items-center mb-2">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
                                                <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
                                            </svg>
                                            <div class="ms-1">ツールバー</div>
                                        </div>
                                        <div class="row">
                                            <div class="col-2 text-center">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-gear-fill rotation" style="cursor: pointer;" viewBox="0 0 16 16" data-bs-toggle="modal" data-bs-target="#settingModal">
                                                    <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
                                                </svg>
                                                <div class="text-secondary fw-bold dropdown-toggle" style="font-size: 12px;">設定</div>
                                            </div>
                                            <div class="col-2 text-center">
                                                <a href="#" class="text-light" onclick="window.open('https://google.com/', '_blank', 'width=800,height=600'); return false;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-file-code rotation" viewBox="0 0 16 16">
                                                        <path d="M6.646 5.646a.5.5 0 1 1 .708.708L5.707 8l1.647 1.646a.5.5 0 0 1-.708.708l-2-2a.5.5 0 0 1 0-.708l2-2zm2.708 0a.5.5 0 1 0-.708.708L10.293 8 8.646 9.646a.5.5 0 0 0 .708.708l2-2a.5.5 0 0 0 0-.708l-2-2z"/>
                                                        <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1z"/>
                                                    </svg>
                                                </a>
                                                <div class="text-secondary fw-bold dropdown-toggle" style="font-size: 12px;">エディタ</div>
                                            </div>
                                            <div class="col-2 text-center">
                                                <div @click="CHaserOnlineClient()">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-plugin rotation" style="cursor: pointer;" viewBox="0 0 16 16">
                                                        <path fill-rule="evenodd" d="M1 8a7 7 0 1 1 2.898 5.673c-.167-.121-.216-.406-.002-.62l1.8-1.8a3.5 3.5 0 0 0 4.572-.328l1.414-1.415a.5.5 0 0 0 0-.707l-.707-.707 1.559-1.563a.5.5 0 1 0-.708-.706l-1.559 1.562-1.414-1.414 1.56-1.562a.5.5 0 1 0-.707-.706l-1.56 1.56-.707-.706a.5.5 0 0 0-.707 0L5.318 5.975a3.5 3.5 0 0 0-.328 4.571l-1.8 1.8c-.58.58-.62 1.6.121 2.137A8 8 0 1 0 0 8a.5.5 0 0 0 1 0Z"/>
                                                    </svg>
                                                </div>
                                                <div class="text-success fw-bold" style="font-size: 12px;">実行</div>
                                            </div>
                                            <div class="col-2 text-center">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-power rotation" style="cursor: pointer;" viewBox="0 0 16 16">
                                                    <path d="M7.5 1v7h1V1h-1z"/>
                                                    <path d="M3 8.812a4.999 4.999 0 0 1 2.578-4.375l-.485-.874A6 6 0 1 0 11 3.616l-.501.865A5 5 0 1 1 3 8.812z"/>
                                                </svg>
                                                <div class="text-danger fw-bold" style="font-size: 12px;">停止</div>
                                            </div>
                                            <div class="col-2 text-center">
                                                <router-link class="text-light" :to="{ name: 'login' }">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-people-fill rotation" viewBox="0 0 16 16">
                                                        <path d="M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1H7Zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm-5.784 6A2.238 2.238 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.325 6.325 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1h4.216ZM4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z"/>
                                                    </svg>
                                                </router-link>
                                                <div class="text-secondary fw-bold" style="font-size: 12px;">ユーザ切替</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- Modal -->
                                <div class="modal" id="settingModal" tabindex="-1" aria-labelledby="settingModalLabel" aria-hidden="true">
                                    <div class="modal-dialog modal-sm modal-dialog-centered modal-dialog-scrollable">
                                        <div class="modal-content modal-body backgroundDarkBlue">
                                            <div class="d-flex align-items-center mb-3">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16" data-bs-toggle="modal">
                                                    <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
                                                </svg>
                                                <div class="ms-2">設定</div>
                                            </div>
                                            <label for="inputServerURL">CHaserOnlineServerURL</label>
                                            <input type="text" v-model="CHaserOnlineServerURL" id="inputServerURL" class="form-control text-bg-dark border-0 p-1 px-2 mb-1" />
                                            <label for="inputProxy">ProxyAddress</label>
                                            <input type="text" v-model="CHaserOnlineProxy" id="inputProxy" class="form-control text-bg-dark border-0 p-1 px-2 mb-3" />
                                            <div class="text-end">
                                                <button class="btn btn-success p-1" @click="sendSetting()" v-if="!settingSendFlag">保存</button>
                                                <button class="btn btn-success p-1 disabled" type="button" disabled v-else>
                                                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                                    送信中
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
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
                                    <!-- メッセージ -->
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
                                            <div class="text-bg-danger rounded" v-else-if="status?.status === 'bad'">> {{ status?.message || fetchAPI?.msg }}</div>
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
        </Transition>
    </div>
</template>

<style>
.v-enter-active,
.v-leave-active {
    transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}

.rotation:hover {
    transform: rotate(1turn);
    transition: 1s;
}

input:focus {
    outline: 0;
}
</style>