<template>
    <div class="page-listing">
          <ticketBox 
        v-for="listing in tickets"
        v-bind:key="listing.id"
        v-bind:listing="listing" />
       
      
    </div>

</template>

<script>
import axios from 'axios'
import ticketBox from '@/components/ticketBox'



export default {
    name: 'ListingPage',
    data() {
        return{
            tickets: []
            
        }

    },
    components: {
      ticketBox
      
    },
    mounted() {
        this.getListings()
    },
    methods: {
        async getListings() {
            const listing_slug = this.$route.params.listing_slug

            await axios
                .get(`/api/v1/listings/${listing_slug}`)
                .then(response => {
                    this.tickets = response.data
                  
                })
                .catch(error => {
                    console.log(error)
                })

        }
    }
}




</script>