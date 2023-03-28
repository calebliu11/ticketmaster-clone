<template>
    <div class="column is-size-4 is-centered ">
        <div class="box">  
            <div class="content">
                <p>
                    <strong class="is-size-4 has-text-weight-semibold">{{ listing.event }}</strong>
                    <br>
                    <span class="is-size-5">{{ listing.date }}</span>
                    <br>
                    <span class="is-size-5">{{ listing.description }}</span>
                    <br>
                    <p class="has-text-weight-semibold is-italic has-text-primary"> Starting from ${{ listing.price }}</p>


                </p>
            </div>    
        
       
           

            <template v-if="$store.state.isAuthenticated">
                <div class="buttons">
                    <nuxt-link class="button is-success is-normal" :to="`/listings/${listing.slug}`">View Tickets</nuxt-link>

                    <nuxt-link class="button is-warning is-normal" :to="`/listings/sell/${listing.slug}`">Sell Ticket</nuxt-link>
                </div>
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

