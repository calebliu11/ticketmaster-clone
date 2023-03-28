<template>
    <div class="login-page">
        <div class="columns">
            <h2 class="title">Login</h2>

            <form @submit.prevent="enterForm">
                <div hidden>{% csrf_token %}</div>
                <div class="field">
                    <label>Username</label>
                    <div class="control">
                        <input type="text" class="input" v-model="username">
                    </div>
                </div>

                <div class="field">
                    <label>Password</label>
                    <!-- <div class="control">
                        <input type="text" class="input" v-model="password">
                    </div> -->
                    <div class="field has-addons">
                        <div class="control is-expanded">
                            <input v-if="showPassword" type="text" class="input" v-model="password" />
                            <input v-else type="password" class="input" v-model="password">
                        </div>
                        <div class="control">
                            <button class="button" type="button" @click="toggleShow" :style="{backgroundColor: show ? 'white' : '#00d1b2', color: show ? 'black' : 'white'}">
                                Show
                            </button>
                        </div>
                    </div>
                </div>

                <div class="error-notification" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="field">
                    <div class="control">
                        <button>Login</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import Cookies from 'js-cookie'

export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            showPassword: false,
            password: '',
            errors: []
        }
    },
    computed: {
        buttonLabel() {
            return (this.showPassword) ? "Hide" : "Show";
        }
    },
    methods: {
        toggleShow() {
            this.showPassword = !this.showPassword;
            this.show = !this.show;
        },
        async enterForm() {
            localStorage.removeItem("token")
            localStorage.removeItem("user")

            const loginFormData = {
                username: this.username,
                password: this.password
            }

            const csrftoken = Cookies.get('csrftoken');
            const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };

            const username = this.username
            
            const id = await $fetch(`/api/v1/users/${username}/id`, { credentials: 'include', method: "GET", headers })
            const user = await $fetch(`/api/v1/users/${id.id}/`, { credentials: 'include', method: "GET", headers })

            await $fetch("api/v1/token/login/", { method: "POST", headers, body: loginFormData })
                .then(response => {
                    const token = response.auth_token
                    this.$store.commit('authenticateUser', token)
                    this.$store.commit('setUser', user)

                    localStorage.setItem("token", token)
                    
                    this.$router.push('/')
                })
                .catch(error => {
                    this.errors.push(error.response._data.non_field_errors)
                    if (error.response) {
                        console.log(JSON.stringify(error.response))

                    }
                    else if (error.message) {
                        this.errors.push('Something went wrong. Please try again!')
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>
