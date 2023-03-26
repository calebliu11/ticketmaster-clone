
<template>
  <div class="home">
        <section class="hero is-small is-primary">
          <div class="hero-body">
            <p class="title">
             Top Upcoming Events
            </p>
            <p class="subtitle">
              Near WashU
            </p>
          </div>
        </section>
     
      <div> 
      <listingBox 
        v-for="listing in recentListings"
        v-bind:key="listing.id"
        v-bind:listing="listing" />
      </div>
    
  </div>
</template>

<script>
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
    },
    methods: {
      async RecentListingsList() {
        await $fetch('/api/v1/recent-listings/', { method: "GET" })
          .then(response => {
            this.recentListings = response
          })
          .catch(error => {
            console.log(error)
          })
      }
      
    }
  }
</script>