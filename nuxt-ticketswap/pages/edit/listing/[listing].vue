<template>
    <div class="column is-12 box">
        <h2 class="title">Edit Listing</h2>
            <form class="mt-3" @submit.prevent="enterForm">
                <div hidden>{% csrf_token %}</div>       

                <div class="field">
                    <label>Update Price ($)</label>
                    <div class="control">
                        <input type="number" class="input" v-model="price">
                    </div>
                </div>

                <div class="error-notification" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="field">
                    <div class="control">
                        <button class="button is-dark">Submit</button>
                        <button @click="$router.push('/my-listings')" class="button ml-4">Back</button>
                    </div>
                </div>            
            </form>
    </div>
</template>

<script>
import Cookies from 'js-cookie'
import { toast } from 'bulma-toast'

export default {
    name: 'EditListing',
    data() {
        return {
            price: null,
            errors: []
        }
    },
    mounted() {
        document.title = 'Ticketswap | Edit Listing'
    },
    methods: {
        enterForm() {
            this.errors = []

            if(this.price < 0) {
                this.errors.push('Price cannot be negative.')
            }

            if(!this.errors.length) {
                const csrftoken = Cookies.get('csrftoken');
                const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };

                $fetch(`/api/v1/edit/listing/${this.$route.params.listing}`, { method: "POST", headers, body: { 'price': this.price }})
                    .then((response) => {
                        console.log(response)
                        toast({
                            message: 'Listing updated!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 1000,
                            position: 'bottom-left',
                        })
                        this.$router.push('/my-listings')
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