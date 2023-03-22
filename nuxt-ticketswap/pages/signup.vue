<template>
    <div class="signup-page">
        <div class="columns">
            <h2 class="title">Sign Up</h2>

            <form @submit.prevent="enterForm">
                <div class="field">
                    <label>Username</label>
                    <div class="control">
                        <input type="text" class="input" v-model="username">
                    </div>
                </div>

                <div class="field">
                    <label>First Name</label>
                    <div class="control">
                        <input type="text" class="input" v-model="first_name">
                    </div>
                </div>

                <div class="field">
                    <label>Last Name</label>
                    <div class="control">
                        <input type="text" class="input" v-model="last_name">
                    </div>
                </div>

                <div class="field">
                    <label>Email</label>
                    <div class="control">
                        <input type="text" class="input" v-model="email">
                    </div>
                </div>

                <div class="field">
                    <label>Password</label>
                    <div class="control">
                        <input type="text" class="input" v-model="password">
                    </div>
                </div>

                <div class="field">
                    <label>Verify Password</label>
                    <div class="control">
                        <input type="text" class="input" v-model="password2">
                    </div>
                </div>

                <div class="error-notification" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="field">
                    <div class="control">
                        <button>Sign up</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignupPage',
    data() {
        return {
            username: '',
            email: '',
            first_name: '',
            last_name: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        enterForm(){
            this.errors = []

                if (this.username === '') {
                    this.errors.push('The username field is required.')
                }

                if (this.password.length < 8) {
                    this.errors.push('Your password must be at least 8 characters long.')
                }

                if (this.password !== this.password2) {
                    this.errors.push('Your passwords must match.')
                }

                if (this.first_name === '') {
                    this.errors.push('The first name field is required.')
                }

                if (this.last_name === '') {
                    this.errors.push('The last name field is required.')
                }

                if (this.email === '') {
                    this.errors.push('The email field is required.')
                }

                if (!this.errors.length) {
                    const formData = {
                        username: this.username,
                        password: this.password,
                        first_name: this.first_name,
                        last_name: this.last_name,
                        email: this.email
                    }

                    $fetch("/api/v1/users/", {method: "POST", body: formData})
                        .then(() => {
                            toast({
                                message: 'Your account was created, please log in!',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 1000,
                                position: 'bottom-left',
                            })
                            this.$router.push('/login')
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
}
</script>
