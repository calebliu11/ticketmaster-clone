<template>
    <tr>
        <td><router-link :to="item.ticket.get_absolute_url">{{ item.ticket.event }}</router-link></td>
        <td>{{ item.ticket.description }}</td>
        <td>${{ item.ticket.price }}</td>
        <td><img :src="imageSrc" alt="My Image" style="height: 300px;"></td>
        <td>{{ item.ticket.user_email }}</td>

        
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
            imageSrc: null,
        }
    },
     created() {
        this.fetchImage();
    },
    methods: {
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        },
        async fetchImage() {
            this.imageSrc = `/api/v1/${this.initialItem.ticket.image}/`;
        },
    },
}
</script>