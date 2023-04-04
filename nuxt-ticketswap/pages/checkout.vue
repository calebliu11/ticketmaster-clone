<template>
<div class="column is-10 box">
        <div v-if="this.cart.items.length">
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Event</th>
                        <th>Description</th>
                        <th>Seller</th>
                        <th>Price</th>
                    </tr>
                </thead>

                <tbody>
                    <tr
                        v-for="item in cart.items"
                        v-bind:key="item.ticket.id"
                    >
                        <td>{{ item.ticket.event }}</td>
                        <td>{{ item.ticket.description }}</td>
                        <td>{{ item.ticket.user_email }}</td>
                        <td>${{ item.ticket.price.toFixed(2) }}</td>
                    </tr>
                </tbody>

                <div v-if="this.cart.items.length > 0" class="column is-10">
                    <h2 class="subtitle has-text-weight-semibold">Order Summary</h2>

                    <h3 class="is-size-4 has-text-weight-semibold">${{ cartPrice.toFixed(2) }}</h3>

                    <p v-if="this.cart.items.length === 1">{{ this.cart.items.length }} ticket</p>
                    <p v-else>{{ this.cart.items.length }} tickets</p>

                </div>
            </table>

            <div class="column is-10 box">
                <h2 class="subtitle">Order Details</h2>

                <div class="field">
                    <label>First name</label>
                    <div class="control">
                        <input type="text" class="input" v-model="first_name">
                    </div>
                </div>

                <div class="field">
                    <label>Last name</label>
                    <div class="control">
                        <input type="text" class="input" v-model="last_name">
                    </div>
                </div>

                <div class="field">
                    <label>Email</label>
                    <div class="control">
                        <input type="text" class="input" v-model="email">
                    </div>
                </div>

            </div>

            <div class="error-notification" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <hr>
            
            <div id="card-element" class="mb-5"></div>

            <button class="button is-dark" @click="enterForm">Pay</button>
        </div>
        <h2 v-else>Your cart is empty</h2>
    </div>
</template>

<script>
import { loadStripe } from '@stripe/stripe-js'

export default {

    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {}, 
            first_name: '',
            last_name: '',
            email: '',
            errors: []

        }
    },
    mounted() {
        this.cart = this.$store.state.cart

        this.stripeSetup()
    },

   
    methods: {
        async stripeSetup() {
            if (this.cart.items.length > 0) {
            this.stripe = await loadStripe('pk_test_51MsvUpB0HmvtCEdiNJEBJrxMhmg0SMS0c7vmh1H1lsSunWBt2UbbpH9jRfA3Cr3iIXoHjJzLWXxW8DPwAF7Qyrtl008leL4DWT')

            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })
            this.card.mount('#card-element')
            }
        },
        enterForm(){
            this.errors = []

            if (this.first_name === '') {
                this.errors.push('First name is required!')
            }

            if (this.last_name === '') {
                this.errors.push('Last name is required!')
            }

            if (this.email === '') {
                this.errors.push('Email is required!')
            }

            if (!this.errors.length) {
                this.stripe.createToken(this.card).then(result => {
                    if (result.error) {
                        this.errors.push("Stripe error. Please try again.")
                        console.log(result.error.message)
                    }
                    else {
                        this.completeCheckout(result.token)
                    }
                })               
            }
        },
        async completeCheckout(token) {
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const ticket = {
                    listing: item.ticket.id,
                    event: item.ticket.event,
                    description: item.ticket.description,
                    price: item.ticket.price,
                    seller_email: item.ticket.user_email,
                    date: item.ticket.date,
                    image_url: item.ticket.image,
                }
                items.push(ticket)
            }
            
            const checkoutData = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'stripe_token': token.id,
                'items': items,
            }

            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token };
            await $fetch('/api/v1/checkout/', { method: "POST", headers, body: checkoutData })
                .then(() => {
                    this.$store.commit('emptyCart')
                    this.$router.push('/success')
                })
                .catch(error => {
                    this.errors.push(error.response._data)
                    console.log(error.response._data)
                })

        },
        async fetchImage() {
            this.imageSrc = `/api/v1/${this.initialItem.ticket.image}/`;
        },
    },
    computed: {
        cartPrice() {
            return this.cart.items.reduce((sum, ticketPrice) => {
                return sum += ticketPrice.ticket.price
            }, 0)
        },
    }
}
</script>