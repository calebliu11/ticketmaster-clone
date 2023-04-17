<template>
    <div class="column is-10">
        <h2 class="title">Cart</h2>
    </div>

    <div class="column is-10 box">
        <table v-if="this.cart.items.length" class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Event</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Seller</th>
                </tr>
            </thead>

            <tbody>
                <CartItem
                    v-for="item in this.cart.items"
                    v-bind:key="item.id"
                    v-bind:initialItem="item"
                    v-on:removeFromCart="removeFromCart" />
            </tbody>
        </table>

        <h2 v-else>Your cart is empty.</h2>
    </div>

    <div v-if="this.cart.items.length > 0" class="column is-10 box">
        <h2 class="subtitle">Order Summary</h2>

        <h3 class="is-size-4 has-text-weight-semibold">${{ cartPrice.toFixed(2) }}</h3>

        <p v-if="this.cart.items.length === 1">{{ this.cart.items.length }} ticket</p>
        <p v-else>{{ this.cart.items.length }} tickets</p>

        <router-link to="/checkout" class="button is-dark">Checkout</router-link>
    </div>
</template>

<script>
import CartItem from '@/components/CartItem'

export default {
    name: 'Cart',
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        console.log(JSON.stringify(this.cart.items))
    },
    components: {
        CartItem
    },
    methods: {
        removeFromCart(item) {
            console.log(JSON.stringify(this.cart.items))
            this.cart.items = this.cart.items.filter(i => i.ticket.id !== item.ticket.id)
            
        }
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