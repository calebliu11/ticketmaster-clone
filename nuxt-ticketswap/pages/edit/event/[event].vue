<template>
    <div class="column is-12 box">
        <h2 class="title">Edit Event:</h2>
            <form class="mt-3" @submit.prevent="enterForm">
                <div hidden>{% csrf_token %}</div>       

                <div class="field">
                    <label>Update Name</label>
                    <div class="control">
                        <input type="text" class="input" v-model="name">
                    </div>
                </div>

                <div class="field">
                    <label>Update Description</label>
                    <div class="control">
                        <input type="text" class="input" v-model="description">
                    </div>
                </div>

                <div class="field mb-4">
                    <label>Update Date</label>
                    <div class="control">
                        <input type="date" class="input" v-model="date">
                    </div>
                </div>

                <span class="has-text-semibold">Update Status</span>
                <br>

                <div class="select mb-4 mt-2">
                    <select v-model="status">
                        <option>ACTIVE</option>
                        <option>CANCELED</option>
                    </select>
                </div>

                <br>
                <span class="has-text-semibold">Update Category</span>
                <br>
                <div class="select mb-4 mt-2">
                    <select id="select-category" v-model="category">
                        <option>Sports</option>
                        <option>Concert</option>
                        <option>Performance</option>
                        <option>Bar</option>
                        <option>Student Group</option>
                        <option>Other</option>
                    </select>
                </div>

                <div class="error-notification" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="field mt-4">
                    <div class="control">
                        <button class="button is-dark">Submit</button>
                        <button @click="$router.push('/account')" class="button ml-4">Back</button>
                    </div>
                </div>            
            </form>
    </div>
</template>

<script>
import Cookies from 'js-cookie'
import { toast } from 'bulma-toast'

export default {
    name: 'EditEvent',
    data() {
        return {
            name: '',
            description: '',
            date: '',
            status: '',
            category: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Ticketswap | Edit Event'
    },
    methods: {
        enterForm() {
            this.errors = []

            const eventDate = new Date(this.date)
            eventDate.setHours(eventDate.getHours() + 5) 
            if (eventDate < new Date()) {
                this.errors.push('Event cannot be in the past!')
                console.log(eventDate)
            }
            
            if (!this.errors.length) {
                const formData = {
                    user: 22,
                    name: this.name,
                    description: this.description,
                    date: this.date,
                    status: this.status,
                    category: this.category,
                }

                const csrftoken = Cookies.get('csrftoken');
                const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };

                $fetch(`/api/v1/edit/event/${this.$route.params.event}`, { method: "POST", headers, body: formData })
                    .then((response) => {
                        console.log(response)
                        toast({
                            message: 'Event updated!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 1000,
                            position: 'bottom-left',
                        })
                        this.$router.push('/my-events')
                    })
                    .catch(error => {
                        if (error.response) {
                            this.errors.push(JSON.stringify(error.response._data))
                            console.log(JSON.stringify(error.response))
                        }
                        else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                            console.log(JSON.stringify(error.message))
                        }
                    })
            }
           
        }
    }
}
</script>