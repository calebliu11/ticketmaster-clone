<template>
    <div class="search-page">
        <div class="columns is-multiline">
            <div class="column is-10">
                <h2 class="title">Search: "{{ query }}"</h2>
            </div>
        </div>

        <template v-if="listings.length > 0">
            <ul v-for="listing in listings">
                <div class="box mb-4">  
                    <div class="content">
                        <p>
                            <strong class="is-size-4 has-text-weight-semibold">{{ listing.event }}</strong>
                            <br>
                            <span class="is-size-5">{{ formattedDate(listing) }}</span>
                            <br>
                            <span class="is-size-5">{{ listing.description }}</span>
                            <br>
                            <p class="has-text-weight-semibold is-italic has-text-primary is-size-4">${{ listing.price }}</p>
                        </p>
                    </div>    
            
                    <template v-if="$store.state.isAuthenticated">
                        <div class="buttons">
                            <a class="button is-dark" @click="addToCart(listing)">Claim Ticket</a>
                        </div>
                    </template>            
                </div>
            </ul>
        </template>
        <template v-else>
            <h2 class="subtitle">
                No listings found for your query!
            </h2>
        </template>
    </div>
</template>

<script>
import { toast } from 'bulma-toast'

export default {
    name: 'Search',
    
    data() {
        return {
            listings: [],
            query: '',
        }
    },
    mounted() {
        let url = window.location.search.substring(1)
        let params = new URLSearchParams(url)

        if (params.get('query')) {
            this.query = params.get('query')

            this.doSearch()
        }
    },
    methods: {
        async doSearch() {
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token };
            await $fetch('/api/v1/search/', { method: "POST", headers, body: { 'query': this.query } })
            .then((response) => {
                this.listings = response
            })
            .catch((error) => console.error(error))
        },
        formattedDate(listing) {
            const date = new Date(listing.date);
            const currentTimeZoneOffset = date.getTimezoneOffset();

            const targetTimeZoneOffset = 800; 
            const timeDifferenceInMinutes = targetTimeZoneOffset - currentTimeZoneOffset;
            const newDate = new Date(date.getTime() + (timeDifferenceInMinutes * 60 * 1000));


            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return newDate.toLocaleDateString('en-US', options);
        },
        addToCart(listing) {
            const item = {
                ticket: listing
            }

            const existsInCart = this.$store.state.cart.items.filter(i => i.ticket.id === item.ticket.id)
            if (!existsInCart.length) {
                this.$store.commit('addToCart', item)
                toast({
                    message: 'Ticket was added to your cart!',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 1000,
                    position: 'bottom-left',
                })
            }
            else {
                toast({
                    message: 'Ticket already exists in your cart!',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 1000,
                    position: 'bottom-left',
                })
            }
        }
    }
}
</script>