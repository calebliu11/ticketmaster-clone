<template>
    <div class="column is-size-4 is-centered ">
        <div class="box">
        
        
            <h3 class="is-size-4 has-text-weight-semibold">{{ listing.event }}</h3>
          
            <p class="is-size-6">{{ listing.description }}</p>
            <p class="is-size-6 has-text-success">${{ listing.price }}</p>
            <router-link v-bind:to="listing.get_absolute_url" class="button is-dark mt-4"> View Tickets</router-link>
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

