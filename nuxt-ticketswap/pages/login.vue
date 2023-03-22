<template>
    <div class="login-page">
        <div class="columns">
            <h2 class="title">Login</h2>

            <form @submit.prevent="enterForm">
                <div class="field">
                    <label>Username</label>
                    <div class="control">
                        <input type="text" class="input" v-model="username">
                    </div>
                </div>

                <div class="field">
                    <label>Password</label>
                    <div class="control">
                        <input type="text" class="input" v-model="password">
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
import axios from 'axios'

export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async enterForm() {
            localStorage.removeItem("token")

            const loginFormData = { 
                username: this.username,
                password: this.password
            }

            await $fetch("api/v1/token/login/", { method: "POST", body: loginFormData} )
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('authenticateUser', token)

                    localStorage.setItem("token", token)
                
                    this.$router.push('/')
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data))

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