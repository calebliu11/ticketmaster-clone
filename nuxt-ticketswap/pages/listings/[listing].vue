<template>
    <div class="page-listing">
        <template v-if="tickets.length > 0">
          <div class="box">  
            <div class="content">
                <p>
                    <strong class="is-size-2 has-text-info has-text-weight-semibold">{{ tickets[0].event }}</strong>
                    <br>
                    <span class="is-size-5">Date: {{ tickets[0].date }}</span>
                    <br>
                    <span class="is-size-5 has-text-weight-semibold is-italic">{{ tickets[0].description }}</span>
                    <br>
                 
              
                </p>
            </div>  
          </div>  
          
        </template>
        <ul v-for="listing in tickets">
          
          <div class="column is-size-4 is-centered ">
            <div class="box">
      

            <p class="is-size-3 has-text-success">${{ listing.price }}</p>

            <p class="is-size-6">Sold by {{ listing.user_email }}</p>
          

            <template v-if="$store.state.isAuthenticated">
              <a class="button is-dark" @click="addToCart(listing)">Claim Ticket</a>
            </template>
           
            </div>
          </div>
        </ul>
    </div>
</template>

<script>
import { toast } from 'bulma-toast'
import listingBox from '@/components/listingBox'
export default {
  data() {
    return{
      tickets: []   
    }
  },
  components: {
    listingBox 
  },
  mounted() {
      this.getListings()
  },
  methods: {
    async getListings() {
      const slug = this.$route.params.listing
      await $fetch(`/api/v1/listings/${slug}`, { method: "GET" })
        .then((response) => {
          this.tickets = response
        })
        .catch((error) => console.error(error))
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