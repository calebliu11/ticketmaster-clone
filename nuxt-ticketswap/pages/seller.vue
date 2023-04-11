<template>
    <div class="container">
        <div class="seller-page">
            <h2 class="title">Sell Ticket</h2>
            <template v-if="$store.state.isAuthenticated">
                <form @submit.prevent="enterForm">
                    <div hidden>{% csrf_token %}</div>
                    <div class="field">
                        <label class="label">Event</label>
                        <div class="control">
                            <input class="input" type="text" v-model="event" placeholder="e.g. WashU LNYF">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Description</label>
                        <div class="control">
                            <textarea class="textarea" v-model="description"
                                placeholder="e.g. LNYF is an annual student-run production in celebration of the Lunar New Year."></textarea>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Price</label>
                        <div class="control has-icons-left">
                            <input class="input" type="number" v-model="price" placeholder="e.g. $10">
                            <span class="icon is-small is-left">
                                <font-awesome-icon icon="fa-solid fa-dollar-sign" beat />

                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Date</label>
                        <div class="control">
                            <input class="input" type="date" v-model="date">
                        </div>
                    </div>

                    <div class="file">
                        <label class="file-label">
                            <input class="file-input" type="file" @change="onChangeFile" name="image">
                            <span class="file-cta">
                                <span class="file-icon">
                                    <font-awesome-icon icon="fa-solid fa-upload" beat />
                                </span>
                                <span class="file-label">
                                    Upload the ticket...
                                </span>
                            </span>
                        </label>
                    </div>

                    <p class="mb-3">
                    </p>

                    <div class="error-notification" v-if="errors.length">
                        <div class="notification is-danger">
                            <button class="delete" @click="clearErrors"></button>
                            <ul>
                                <li v-for="error in errors" :key="error">{{ error }}</li>
                            </ul>
                        </div>
                    </div>

                    <p class="mb-3">
                    </p>

                    <div class="field">
                        <div class="control">
                            <button class="button is-primary" :disabled="isSubmitting">Submit</button>
                        </div>
                    </div>
                </form>
            </template>

            <template v-else>
                <h3 class="is-size-4 has-text-weight-semibold">You must be logged in to sell a ticket!</h3>
            </template>
        </div>
    </div>
</template>
  

  

<script>
import { toast } from 'bulma-toast'
import Cookies from 'js-cookie'

export default {
    name: 'PostListing',
    data() {
        return {
            user: null,
            user_email: '',
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

        clearErrors() {
            this.errors = []
        },


        enterForm() {
            this.errors = []
            let finalDate = ""

            if (!this.event) {
                this.errors.push('The event field is required.')
            }

            if (!this.date) {
                this.errors.push('The date field is required.')
            } else {
                console.log(this.date)
                const dateSplit = this.date.split('-');
                const dateReformatted = new Date(dateSplit[0], dateSplit[1]-1, dateSplit[2], 0, 0, 0, 0);
                const today = new Date();
                const todayReformatted = new Date(today.getFullYear(), today.getMonth(), today.getDate(), 0, 0, 0, 0);

                finalDate = this.date;

                if (dateReformatted < todayReformatted) {
                    this.errors.push('The date cannot be in the past.')
                } else if (dateReformatted > todayReformatted) {
                    console.log('entered date is after today');
                } else {
                    console.log('entered date is equal to today');
                }
            }

            if (this.price < 0) {
                this.errors.push('Price cannot be negative.')
            }
            if (!this.price) {
                this.errors.push('The price field is required.')
            }

            if (!this.image) {
                this.errors.push('You must upload a ticket.')
            }

            if (!this.errors.length) {
                console.log("DATE IN FORM")
                console.log(finalDate); // console says correct date at this line but when you date changes by one day in form data.
                const formData = {
                    user: 8,
                    user_email: 'seller@wustl.edu',
                    event: this.event,
                    description: this.description,
                    price: this.price,
                    date: finalDate, // api changing date here 
                    image: this.image,
                }

                const csrftoken = Cookies.get('csrftoken');
                const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };

                $fetch("/api/v1/post-listing/", { method: "POST", headers, body: formData })
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