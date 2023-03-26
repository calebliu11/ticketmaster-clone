import { createStore } from 'vuex'

export default createStore({
    state: {
        isAuthenticated: false,
        token: '',
        isLoading: false,
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
        },
        authenticateUser(state, token) {
            state.isAuthenticated = true
            state.token = token
        },
        deauthenticateUser(state){
            state.isAuthenticated = false
            state.token = ''
        },
    },
    actions: {
    },
    modules: {
    }
})