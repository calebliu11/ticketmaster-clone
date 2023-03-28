<template>
    <div class="column is-size-4 is-centered ">
        <div class="box">      
        
            <h3 class="is-size-4 has-text-weight-semibold">{{ listing.event }}</h3>

            <p class="is-size-6">{{ listing.description }}</p>

            <p class="is-size-6 has-text-success">${{ listing.price }}</p>

            <p class="is-size-6">{{ listing.date }}</p>

            <template v-if="$store.state.isAuthenticated">
                <nuxt-link class="button is-dark" :to="`/listings/${listing.slug}`">View Ticket</nuxt-link>
            </template>
        </div>
    </div>
</template>

<script>
export default {
    name: 'listingBox',
    props: {
        listing: Object
    }
}
</script>

