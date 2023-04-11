<template>
    <div class="column is-size-4 is-centered ">
        <div class="box">  
            <div class="content">
                <p>
                    <strong class="is-size-4 has-text-weight-semibold">{{ listing.event }}</strong>
                    <br>
                    <span class="is-size-5">{{ formattedDate }}</span>
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
            <template v-else="$store.state.isAuthenticated">
                <div class="buttons">
                    <nuxt-link class="button is-success is-normal" :to="'/login'">Login To View Tickets</nuxt-link>

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
    }, 
    computed: {
    formattedDate() {
        const date = new Date(this.listing.date);
        const currentTimeZoneOffset = date.getTimezoneOffset();

        const targetTimeZoneOffset = 800; 
        const timeDifferenceInMinutes = targetTimeZoneOffset - currentTimeZoneOffset;
        const newDate = new Date(date.getTime() + (timeDifferenceInMinutes * 60 * 1000));


        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return newDate.toLocaleDateString('en-US', options);
    }
  }
    
}
</script>

