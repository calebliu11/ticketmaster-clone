<template>
    <div class="seller-page">  
            <h2 class="title">Create New Event</h2>
            <template v-if="$store.state.isAuthenticated">

                <form @submit.prevent="enterForm">
                    <div hidden>{% csrf_token %}</div>

                    <div class="field">
                        <label class="label">Event</label>
                        <div class="control">
                            <input type="text" class="input" v-model="event">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Description</label>
                        <div class="control">
                            <input type="text" class="input" v-model="description">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Date</label>
                        <div class="control">
                            <input type="date" class="input" v-model="date">
                        </div>
                    </div>

                    <div class="error-notification" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-primary" :disabled="isSubmitting">Submit</button>
                        </div>
                    </div>
                </form>
            </template>

            <template v-else>
                <h3 class="is-size-4 has-text-weight-semibold">You must be logged in to create an event!</h3>
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
            name: '',
            description: '',
            date: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Ticketswap | Create New Event'
    },
    methods: {
        enterForm(){
            this.errors = []

                if (this.event === '') {
                    this.errors.push('The event field is required.')
                }
                
                const eventDate = new Date(this.date)
                eventDate.setHours(eventDate.getHours() + 5) 
                if (eventDate < new Date()) {
                    this.errors.push('Event cannot be in the past!')
                    console.log(eventDate)
                }

                if (!this.errors.length) {
                    const formData = {
                        user: 22,
                        user_username: 'admin',
                        name: this.event,
                        description: this.description,
                        date: this.date,
                    }
                    
                    const csrftoken = Cookies.get('csrftoken');
                    const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };
                    
                    $fetch("/api/v1/create-event/", { method: "POST", headers, body: formData} )
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
                                this.errors.push(error.response._data.errors)
                                console.log(JSON.stringify(error.response))
                            }
                            else if (error.message) {
                                this.errors.push('Something went wrong. Please try again!')
                                console.log(JSON.stringify(error))
                            }
                        })
                    
                }
        }
    },
}
</script>