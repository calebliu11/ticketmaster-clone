import { createWebHistory, createRouter } from "vue-router";

import BuyerPage from "./apps/BuyerPage.vue"
import SellerPage from "./apps/SellerPage.vue"

const routes = [
    {
        path: '/buyer',
        component: BuyerPage
    },
    {
        path: '/seller',
        component: SellerPage
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;