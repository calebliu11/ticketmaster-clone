<template>
    <div class="search-page">
        <div class="columns is-multiline">
            <div class="column is-10">
                <h2 class="title"> Search: "{{ query }}"</h2>
            </div>
        </div>

        <template v-if="listings.length > 0">
            <listingBox 
            v-for="listing in listings"
            v-bind:key="listing.id"
            v-bind:listing="listing" />
        </template>
        <template v-else>
            <h2 class="subtitle">
                No listings found for your query!
            </h2>
        </template>
    </div>
</template>

<script>
import listingBox from '@/components/listingBox'

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
            }
    }
}


</script>