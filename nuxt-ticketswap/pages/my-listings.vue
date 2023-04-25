<template>
    <div class="listings-list">
      <br>
      <h2 class="title">My Listings</h2>
        <ul v-for="listing in listings">
          <div v-if="listing.status=='SOLD'" class="box mt-5 has-background-grey-lighter">  
            <div class="content">
                <strong class="is-size-4 has-text-weight-semibold">{{ listing.event_name }}</strong>
                <br>
                <span class="is-size-5">{{ computeFormattedDate(listing) }}</span>
                <br>
                <span class="is-size-5 has-text-info">{{ listing.event_description }}</span>
                <br>
                <span class="is-size-5 has-text-weight-bold">{{ listing.status }}</span>
                <br>
                <p class="has-text-weight-semibold is-italic has-text-primary">${{ listing.price }}</p>
                <br>
                <p class="has-text-weight-semibold is-italic">ID: {{ listing.id }}</p>

              </div>    
            </div>
            <div v-else-if="dateInPast(listing)" class="box mt-5 has-background-grey-lighter">
              <div class="content">
                <strong class="is-size-4 has-text-weight-semibold">{{ listing.event_name }}</strong>
                <br>
                <span class="is-size-5">{{ computeFormattedDate(listing) }}</span>
                <br>
                <span class="is-size-5 has-text-info">{{ listing.event_description }}</span>
                <br>
                <span class="is-size-5 has-text-weight-bold">EXPIRED</span>
                <br>
                <p class="has-text-weight-semibold is-italic has-text-primary">${{ listing.price }}</p>
                <br>
                <p class="has-text-weight-semibold is-italic">ID: {{ listing.id }}</p>

              </div>    
            </div>
            <div v-else class="box mt-5">  
                <div class="content">
                    <strong class="is-size-4 has-text-weight-semibold">{{ listing.event_name }}</strong>
                    <br>
                    <span class="is-size-5">{{ computeFormattedDate(listing) }}</span>
                    <br>
                    <span class="is-size-5 has-text-info">{{ listing.event_description }}</span>
                    <br>
                    <span class="is-size-5 has-text-weight-bold">{{ listing.status }}</span>
                    <br>
                    <p class="has-text-weight-semibold is-italic has-text-primary">${{ listing.price }}</p>
                    <br>
                    <p class="has-text-weight-semibold is-italic">ID: {{ listing.id }}</p>

                    <button @click="$router.push('/edit/listing/' + listing.slug)" class="button is-primary">Edit Listing</button>
                    <button @click="deleteListing(listing)" class="button is-danger ml-4">Delete Listing</button>
                </div>    
            </div>
        </ul>
    </div>
</template>

<script>
import { toast } from 'bulma-toast'

export default {
  data() {
      return {
          listings: [],
          events: {}
      }
  },
  mounted() {
    this.getListings()
    document.title = 'Ticketswap | My Listings'
  },
  methods: {
    async getListings() {
      const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
      await $fetch("api/v1/listings/", { method: "GET", headers })
      .then((response) => {
        this.listings = response
        console.log(JSON.stringify(this.listings))
      })
      .catch((error) => console.error(error))
    },
    computeFormattedDate(listing) {
      const date = new Date(listing.event_date);
      const currentTimeZoneOffset = date.getTimezoneOffset();

      const targetTimeZoneOffset = 800; 
      const timeDifferenceInMinutes = targetTimeZoneOffset - currentTimeZoneOffset;
      const newDate = new Date(date.getTime() + (timeDifferenceInMinutes * 60 * 1000));

      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return newDate.toLocaleDateString('en-US', options);
    },
    dateInPast(listing){
      const eventDate = new Date(listing.event_date)
      eventDate.setHours(eventDate.getHours() + 29) 
      return eventDate < new Date()
    },
    deleteListing(listing) {
    const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
      $fetch(`api/v1/delete/listing/${listing.slug}`, { method: "POST", headers, body: { } })
      .then((response) => {
        console.log(response)
        toast({
          message: "Listing successfully deleted!",
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 1500,
          position: 'bottom-left',
        })
        this.$router.push('/account')
      })
      .catch((error) => console.error(error))
    }
  }
}
</script>