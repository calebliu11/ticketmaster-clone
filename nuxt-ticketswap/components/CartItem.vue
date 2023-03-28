<template>
    <tr>
        <td><router-link :to="item.listing.get_absolute_url">{{ item.listing.event }}</router-link></td>
        <td>{{ item.listing.description }}</td>
        <td>${{ item.listing.price }}</td>
        
        <td><img :src="imageSrc" alt="My Image"></td>
        
           
      
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
import axios from 'axios';

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
            this.imageSrc = `/api/v1/${this.initialItem.listing.image}/`;
        },
    },
}
</script>