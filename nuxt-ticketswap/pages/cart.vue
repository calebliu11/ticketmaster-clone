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
                </tr>
            </thead>

            <tbody>
                <CartItem
                    v-for="item in cart.items"
                    v-bind:key="item.listing.id"
                    v-bind:initialItem="item"
                    v-on:removeFromCart="removeFromCart" />
            </tbody>
        </table>

        <h2 v-else>Your cart is empty.</h2>
    </div>

    <div class="column is-10 box">
        <h2 class="subtitle">Order Summary</h2>

        <h3 class="is-size-4 has-text-weight-semibold">${{ cartPrice }}</h3>

        <p v-if="this.cart.items.length === 1">{{ this.cart.items.length }} ticket</p>
        <p v-else>{{ this.cart.items.length }} tickets</p>

        <router-link to="/cart/checkout" class="button is-dark">Checkout</router-link>
    </div>
</template>

<script>
import CartItem from '@/components/CartItem'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.listing.id !== item.listing.id)
        }
    },
    computed: {
        cartPrice() {
            return this.cart.items.reduce((sum, ticketPrice) => {
                return sum += ticketPrice.listing.price
            }, 0)
        },
    }
}
</script>