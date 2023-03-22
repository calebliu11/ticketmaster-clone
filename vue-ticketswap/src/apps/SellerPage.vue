<template>
    <div class="seller-page">
       
            <h2 class="title">Sell Ticket</h2>
            <h4 class="is-size-6">Instructions: For now, in the description add your venmo and email that a buyer should contact you for ticket.</h4>
            <form @submit.prevent="enterForm">
               
               

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
        
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'PostListing',
    data() {
        return {
            event: '',
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
                    this.errors.push('The event field formis required.')
                }

                if(this.price < 0) {
                    this.errors.push('Price cannot be negative.')
                }

                if (!this.errors.length) {
                    const formData = {
                        
                        event: this.event,
                        description: this.description,
                        price: this.price,
                        date: this.date,
                        image: this.image

                    }
                   
                    axios
                        .post("/api/v1/post-listing/", formData, {
                            headers: {
                            'Content-Type': 'multipart/form-data'
                            }
                        })
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
    },
  
}
</script>