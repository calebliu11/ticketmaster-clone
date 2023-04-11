<template>
    <div class="signup-page">
       
            <h2 class="title">Sign Up</h2>

            <form @submit.prevent="enterForm">
                <div hidden>{% csrf_token %}</div>
                <div class="field">
                    <label>Username</label>
                    <div class="control">
                        <input type="text" class="input" v-model="username">
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

                <div class="field">
                    <label>Verify Password</label>

                    <div class="field has-addons">
                        <div class="control is-expanded">
                            <input v-if="showPassword2" type="text" class="input" v-model="password2" />
                            <input v-else type="password" class="input" v-model="password2">
                        </div>
                        <div class="control">
                            <button class="button" type="button" @click="toggleShow2" :style="{backgroundColor: show2 ? 'white' : '#00d1b2', color: show2 ? 'black' : 'white'}">
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
                        <button>Sign up</button>
                    </div>
                </div>
            </form>
        </div>
    
</template>

<script>
import { toast } from 'bulma-toast'
import Cookies from 'js-cookie'

export default {
    name: 'SignupPage',
    data() {
        return {
            username: '',
            email: '',
            first_name: '',
            last_name: '',
            showPassword: false,
            showPassword2: false,
            password: '',
            password2: '',
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
        toggleShow2() {
            this.showPassword2 = !this.showPassword2;
            this.show2 = !this.show2;
        },
        enterForm() {
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

            if (this.email === '') {
                this.errors.push('The email field is required.')
            }

            if(!this.email.includes("@wustl.edu")) {
                this.errors.push('A WashU email is required.')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password,
                    email: this.email
                }

                const csrftoken = Cookies.get('csrftoken');
                const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };

                $fetch("/api/v1/users/", { method: "POST", headers, body: formData })
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
                            this.errors.push(JSON.stringify(error.response._data))
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
}
</script>
