<template>
    <div class="seller-page">  
            <h2 class="title">Sell Ticket</h2>
            <h4 class="is-size-6">Instructions: For now, in the description add your venmo and email that a buyer should contact you for ticket.</h4>
            <form @submit.prevent="enterForm">
                <div hidden>{% csrf_token %}</div>

                <div class="field">
                    <label>Event</label>
                    <div class="control">
                        <input type="text" class="input" v-model="event">
                    </div>
                </div>

                <div class="field">
                    <label>Description</label>
                    <div class="control">
                        <input type="text" class="input" v-model="description">
                    </div>
                </div>

                <div class="field">
                    <label>Price</label>
                    <div class="control">
                        <input type="number" class="input" v-model="price">
                    </div>
                </div>

                <div class="field">
                    <label>Date</label>
                    <div class="control">
                        <input type="date" class="input" v-model="date">
                    </div>
                </div>

                <div class="error-notification" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="field">
                    <div class="control">
                        <button>Submit</button>
                    </div>
                </div>
            </form>
        
    </div>
</template>

<script>
import { toast } from 'bulma-toast'
import Cookies from 'js-cookie'

export default {
    name: 'PostListing',
    data() {
        return {
            event: '',
            description: '',
            price: '',
            date: '',
            errors: []
        }
    },
    methods: {
        enterForm(){
            this.errors = []

                if (this.event === '') {
                    this.errors.push('The event field is required.')
                }

                if(this.price < 0) {
                    this.errors.push('Price cannot be negative.')
                }
                
                const token = this.$store.state.token
                console.log(token)
                if(token === '') {
                    this.errors.push('User is not logged in!')
                }

                if (!this.errors.length) {
                    const formData = {
                        event: this.event,
                        description: this.description,
                        price: this.price,
                        date: this. date,
                    }
                    
                    const csrftoken = Cookies.get('csrftoken');
                    const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };

                    $fetch("/api/v1/post-listing/", { method: "POST", headers, body: formData} )
                        .then(() => {
                            toast({
                                message: 'Your listing was created!',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 1000,
                                position: 'bottom-left',
                            })
                            this.$router.push('/')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response) {
                                    this.errors.push(`${property}: ${error.response[property]}`)
                                }
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