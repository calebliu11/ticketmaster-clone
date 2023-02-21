import { createWebHistory, createRouter } from "vue-router";

import BuyerPage from "./apps/BuyerPage.vue"
import SellerPage from "./apps/SellerPage.vue"
import AboutPage from "./apps/aboutPage.vue"
import AccountPage from "./apps/accountPage.vue"



const routes = [
    {
        path: '/buyer',
        component: BuyerPage
    },
    {
        path: '/seller',
        component: SellerPage
    },
    {
        path: '/about',
        component: AboutPage
    
    },
    {
        path: '/account',
        component: AccountPage
    
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;