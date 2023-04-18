
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
      <eventBox 
        v-for="event in recentEvents"
        v-bind:key="event.id"
        v-bind:event="event" />
      </div>
    
  </div>
</template>

<script>
  import eventBox from '@/components/eventBox'

  export default {
    name: 'HomePage',
    data() {
      return {
        recentEvents: []
      }
    },
    components: {
      eventBox
    },
    mounted() {
      this.RecentListingsList()
      document.title = 'Ticketswap'
    },
    methods: {
      async RecentListingsList() {
        await $fetch('/api/v1/recent-events/', { method: "GET" })
          .then(response => {
            this.recentEvents = response
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      }
      
    }
  }
</script>