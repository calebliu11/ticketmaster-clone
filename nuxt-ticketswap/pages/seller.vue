<template>
    <div class="seller-page">  
            <h2 class="title">Sell Ticket</h2>
            <template v-if="$store.state.isAuthenticated">

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

                    <div class="field">
                        <label>Post Ticket</label>
                            <div class="control">
                                <input type="file" @change="onChangeFile" name="image">
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
            </template>

            <template v-else>
                <h3 class="is-size-4 has-text-weight-semibold">You must be logged in to sell a ticket!</h3>
            </template>
        
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
            user_email: '',
            description: '',
            price: '',
            date: '',
            image: null,
            errors: []
        }
    },
    methods: {
        onChangeFile(event) {
            const reader = new FileReader();
            reader.readAsDataURL(event.target.files[0]);
            reader.onload = () => {
                this.image = reader.result;
            };
        },
        enterForm(){
            this.errors = []

                if (this.event === '') {
                    this.errors.push('The event field is required.')
                }

                if(this.price < 0) {
                    this.errors.push('Price cannot be negative.')
                }
                
                if (!this.errors.length) {
                    const formData = {
                        event: this.event,
                        user_email: this.$store.state.user.email,
                        description: this.description,
                        price: this.price,
                        date: this.date,
                        image: this.image,
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