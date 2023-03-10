<template>
    <div class="seller-page">
       
            <h2 class="title">Sell Ticket</h2>
            <h4 class="is-size-6">Instructions: For now, in the description add your venmo and email that a buyer should contact you for ticket.</h4>
            <form @submit.prevent="enterForm">
                <div class="field">
                    <label>id</label>
                    <div class="control">
                        <input type="number" class="input" v-model="id">
                    </div>
                </div>

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
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'PostListing',
    data() {
        return {
            id: '',
            event: '',
            description: '',
            price: '',
            errors: []
        }
    },
    methods: {
        enterForm(){
            this.errors = []

                if (this.id === '') {
                    this.errors.push('The id field is required.')
                }

                if (this.event === '') {
                    this.errors.push('The event field is required.')
                }

                if(this.price < 0) {
                    this.errors.push('Price cannot be negative.')
                }

                if (!this.errors.length) {
                    const formData = {
                        id: this.id,
                        event: this.event,
                        description: this.description,
                        price: this.price,
                   
                    }

                    axios
                        .post("/api/v1/post-listing/", formData)
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