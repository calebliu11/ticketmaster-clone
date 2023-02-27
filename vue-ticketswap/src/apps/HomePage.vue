
<template>
  <div class="home">
    

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Upcoming Events</h2>
      </div>
      <div> 
      <listingBox 
        v-for="listing in recentListings"
        v-bind:key="listing.id"
        v-bind:listing="listing" />

      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import listingBox from '@/components/listingBox'

 
  export default {
    name: 'HomePage',
    data() {
      return {
        recentListings: []
      }
    },
    components: {
      listingBox
      
    },
    mounted() {
      this.RecentListingsList()
      document.title = 'Home | Djackets'
    },
    methods: {
      async RecentListingsList() {
        await axios
          .get('/api/v1/recent-listings/')
          .then(response => {
            this.recentListings = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }

</script>