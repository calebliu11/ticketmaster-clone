<template>
    <div class="signup-page">
       
            <h2 class="title">Sign Up</h2>

            <form @submit.prevent="enterForm">
                <div hidden>{% csrf_token %}</div>
                <div class="field">
                    <label>Username</label>
                    <div class="control">
                        <input type="text" class="input" v-model="username" name="username">
                    </div>
                </div>

                <div class="field">
                    <label>Email</label>
                    <div class="control">
                        <input type="text" class="input" v-model="email" name="email">
                    </div>
                </div>

                <div class="field">
                    <label>Password</label>

                    <div class="field has-addons">
                        <div class="control is-expanded">
                            <input v-if="showPassword" type="text" class="input" v-model="password1" name="password1"/>
                            <input v-else type="password" class="input" v-model="password1" name="password1">
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
                            <input v-if="showPassword2" type="text" class="input" v-model="password2" name="password2"/>
                            <input v-else type="password" class="input" v-model="password2" name="password2">
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
                        <button type="submit" class="button is-primary">Sign up</button>
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
            password1: '',
            password2: '',
            showPassword: false,
            showPassword2: false,
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
        async enterForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username field is required.')
            }

            if (this.password1.length < 8) {
                this.errors.push('Your password must be at least 8 characters long.')
            }

            if (this.password1 !== this.password2) {
                this.errors.push('Your passwords must match.')
            }

            if (this.email === '') {
                this.errors.push('The email field is required.')
            }

            if(!this.email.includes("@wustl.edu")) {
                this.errors.push('A WashU email is required.')
            }

            if (!this.errors.length) {
   
                const csrftoken = Cookies.get('csrftoken');
                const boundary = '-------------------------' + Math.random().toString(36).substring(2);

                const headers = {'X-CSRFToken': csrftoken };

                const formData = new FormData()
                console.log(this.username)
                formData.append('username', this.username)
                formData.append('email', this.email)
                formData.append('password1', this.password1)
                formData.append('password2', this.password2)

                
                await $fetch("/api/v1/signup/", { method: "POST", headers, body: formData })
                    .then(() => {
                        toast({
                            message: "Please go to your email inbox and click on the activation link to verify your account. Make sure to check your spam folder.!",
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 3500,
                            position: 'bottom-left',
                        })
                        this.$router.push('/login')
                    })
                    .catch(error => {
                        if (error.response) {
                            this.errors.push(error.response._data.errors)
                            console.log(JSON.stringify(error.response._data.errors))
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
