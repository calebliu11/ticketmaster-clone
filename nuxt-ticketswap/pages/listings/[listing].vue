<template>
  <div class="page-listing">
    <router-link to="/" tag="button" class="button is-danger">Return to Home Page</router-link>
      <div v-if="event.status=='CANCELED'" >
        <h3 class="is-size-4 has-text-weight-semibold">This event has been canceled!</h3>

        <p>Check back here or contact the event organizer for updates.</p>
      </div>
      <div v-else-if="tickets.length > 0">
        <div class="box">  
          <div class="content">
              <p>
                  <strong class="is-size-2 has-text-info has-text-weight-semibold">{{ event.name }}</strong>
                  <br>
                  <span class="is-size-5">{{ formattedDate }}</span>
                  <br>
                  <span class="is-size-5 has-text-weight-semibold is-italic">{{ event.description }}</span>
                  <br>
                  <span class="is-size-6 has-text-weight-semibold is-italic">Event Organizer: {{ event.user_username }}</span>

                  
              </p>

             
          </div>  
        </div>  
        
      </div>
      
      <div v-else>
        <div class="box">  
          <div class="content">
              <p>
                  <strong class="is-size-2 has-text-info has-text-weight-semibold">{{ event.name }}</strong>
                  <br>
                  <span class="is-size-5">{{ formattedDate }}</span>
                  <br>
                  <span class="is-size-5 has-text-weight-semibold is-italic">{{ event.description }}</span>
                  <br>
                  <span class="is-size-6 has-text-weight-semibold is-italic">Event Organizer: {{ event.user_username }}</span>
              </p>
          </div>  
        </div>  

        <div class="box">  
          <div class="content">
              <p>
                  <strong class="is-size-5 has-text-weight-semibold">No tickets exist for this event!</strong>
                  <br>
                  <span class="is-size-5 has-text-weight-semibold is-italic"><nuxt-link :to="`/listings/sell/${event.slug}`">Post a listing here.</nuxt-link></span>

                  <br>

                  <span class="is-size-6 is-italic">Note: Your own listings can only be viewed from your account in your My Listings page.</span>


              </p>
          </div>  
        </div>  
        
      </div>

      <ul v-for="listing in tickets">
        
        <div class="column is-size-4 is-centered ">
          <div class="box">
    

          <p class="is-size-3 has-text-success">${{ listing.price }}</p>

          <p class="is-size-3">Seller: {{ listing.user_username }}</p>

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
export default {
data() {
  return{
    event: '',
    tickets: []    
  }
},
mounted() {
    this.getListings(),
    this.getEvent()
    document.title = 'Ticketswap'
},
methods: {
  async getEvent() {
    const slug = this.$route.params.listing
    await $fetch(`/api/v1/get-event/${slug}`, { method: "GET" })
      .then((response) => {
        this.event = response[0]
      })
      .catch((error) => console.error(error))
  },
  async getListings() {
    const slug = this.$route.params.listing
    
    await $fetch(`/api/v1/listings/${slug}`, { method: "GET" })
      .then((response) => {
        this.tickets = response
        console.log(this.tickets)
      })
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
},
computed: {
  formattedDate() {
        const date = new Date(this.event.date);
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

