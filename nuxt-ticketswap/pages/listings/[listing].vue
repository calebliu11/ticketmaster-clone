<template>
    <div class="page-listing">
        <ul v-for="listing in tickets">
          <div class="column is-size-4 is-centered ">
            <div class="box">
             
            <h3 class="is-size-4 has-text-weight-semibold">{{ listing.event }}</h3>

            <p class="is-size-6">{{ listing.description }}</p>

            <p class="is-size-6 has-text-success">${{ listing.price }}</p>
                   
            <a class="button is-dark">Claim Ticket</a>
           
            </div>
          </div>
        </ul>
    </div>
</template>

<script>
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
    }
  } 
}

</script>