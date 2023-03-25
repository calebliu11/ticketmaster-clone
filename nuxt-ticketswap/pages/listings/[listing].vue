<template>
    <div class="page-listing">
      <listingBox 
        v-for="listing in tickets"
        v-bind:key="listing.id"
        v-bind:listing="listing" />
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