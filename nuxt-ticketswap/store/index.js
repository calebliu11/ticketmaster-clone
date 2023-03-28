import { createStore } from 'vuex'

export default createStore({
    state: {
        cart: {
            items: [],
        },
        isAuthenticated: false,
        token: '',
        user: null,
    },
    mutations: {
        initializeStore(state){
            if(localStorage.getItem('token')) {
                state.isAuthenticated = true
                state.token = localStorage.getItem('token')
            }
            else {
                state.isAuthenticated = false
                state.token = ''
            }

            if(localStorage.getItem('user')) {
                state.user = JSON.parse(localStorage.getItem('user'))
            } else {
                localStorage.setItem('user', JSON.stringify(state.user))
            }
            
            if (localStorage.getItem('cart')) {
                state.cart = JSON.parse(localStorage.getItem('cart'))
            } else {
                localStorage.setItem('cart', JSON.stringify(state.cart))
            }
        
        },
        setUser(state, user) {
            state.user = user
            localStorage.setItem('user', JSON.stringify(state.user))
        },
        removeUser(state) {
            state.user = null
            localStorage.setItem('user', JSON.stringify(state.user))
        },
        authenticateUser(state, token) {
            state.isAuthenticated = true
            state.token = token
        },
        deauthenticateUser(state){
            state.isAuthenticated = false
            state.token = ''
        },
        addToCart(state, item) {
            state.cart.items.push(item)
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
        emptyCart(state) {
            state.cart = { items: [] }
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
    },
    actions: {
    },
    modules: {
    }
})