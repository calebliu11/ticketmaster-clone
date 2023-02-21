import { createWebHistory, createRouter } from "vue-router";

import BuyerPage from "./apps/BuyerPage.vue"
import SellerPage from "./apps/SellerPage.vue"
import AboutPage from "./apps/aboutPage.vue"


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
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;