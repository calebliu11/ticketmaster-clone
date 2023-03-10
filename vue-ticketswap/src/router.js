import { createWebHistory, createRouter } from "vue-router";

import BuyerPage from "./apps/BuyerPage.vue"
import SellerPage from "./apps/SellerPage.vue"
import AboutPage from "./apps/aboutPage.vue"
import AccountPage from "./apps/accountPage.vue"
import SignupPage from "./apps/SignupPage.vue"
import HomePage from './apps/HomePage.vue'
import LoginPage from "./apps/LoginPage.vue"
import ListingPage from "./apps/listingPage.vue"

const routes = [
    {
        path: '/',
        component: HomePage
    },
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
    {
        path: '/signup',
        component: SignupPage
    },
    {
        path: '/login',
        component: LoginPage
    },
    {
        path: '/listings/:listing_slug',
        component: ListingPage
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;