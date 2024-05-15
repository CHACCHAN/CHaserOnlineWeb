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
        },
        {
            path: '/auth',
            component: () => import('./components/pages/auth/authPage.vue'),
            children: [
                {
                    path: 'login',
                    name: 'login',
                    component: () => import('./components/pages/auth/loginPage.vue'),
                },
                {
                    path: 'register',
                    name: 'register',
                    component: () => import('./components/pages/auth/registerPage.vue'),
                },
            ]
        }
    ]
});