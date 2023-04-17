<template>
    <tr>
        <td><router-link :to="`/listings/${item.ticket.slug}`">{{ item.ticket.event_name }}</router-link></td>
        <td>{{ item.ticket.event_description }}</td>
        <td>${{ item.ticket.price }}</td>
        <td>{{ item.ticket.user_username }}</td>

        
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem,
        }
    },
    methods: {
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        },
    },
}
</script>