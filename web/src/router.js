import { createRouter, createWebHistory} from 'vue-router';

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'index',
            component: () => import('./components/indexPage.vue'),
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('./components/aboutPage.vue'),
        }
    ]
});