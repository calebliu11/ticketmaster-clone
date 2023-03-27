<template>
    <div class="columns is-multiline">
        <div class="column is-10">
            <h2 class="title">Checkout</h2>
        </div>

        <div class="column is-10">
            
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Event</th>
                        <th>Description</th>
                        <th>Price</th>
                    </tr>
                </thead>

                <tbody>
                    <tr
                        v-for="item in cart.items"
                        v-bind:key="item.listing.id"
                    >
                        <td>{{ item.listing.event }}</td>
                        <td>{{ item.listing.description }}</td>
                        <td>${{ item.listing.price }}</td>
                    </tr>
                </tbody>

                <tfoot>
                    <tr class="column is-10 box-fullwidth">
                        <h2 class="subtitle"><strong>Total:</strong></h2>
                        <h3 class="is-size-4 has-text-weight-semibold">${{ cartPrice.toFixed(2) }}</h3>

                        <p v-if="this.cart.items.length === 1">{{ this.cart.items.length }} ticket</p>
                        <p v-else>{{ this.cart.items.length }} tickets</p>
                    </tr>
                </tfoot>
            </table>

            <div class="column is-12 box">
                <h2 class="subtitle has-text-weight-semibold">Shipping Details</h2>
            </div>

            

        </div>
    </div>
</template>

<script>
export default {
    name: 'Checkout',
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
    computed: {
        cartPrice() {
            return this.cart.items.reduce((sum, ticketPrice) => {
                return sum += ticketPrice.listing.price
            }, 0)
        },
    }
}
</script>