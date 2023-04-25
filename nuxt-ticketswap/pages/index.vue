
<template>
  <!-- <div class="home"> -->
    <section class="hero is-medium has-background-image">
      <div class="hero-body">
        <div class="container">
          <h1 class="title is-size-1 has-text-white has-text-centered">
            <span class="highlighted-title">Find WashU Tickets</span>
          </h1>
          <template v-if="$store.state.isAuthenticated">
          <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control is-expanded">
                <input type="text" class="input" placeholder='Search' name="query">
              </div>

              <div class="control">
                <button class="button is-info">
                  Search
                </button>
              </div>
            </div>
          </form>
        </template>
        </div>
      </div>
    </section>
     
      <div class="event-grid"> 
        <eventBox 
          v-for="event in recentEvents"
          v-bind:key="event.id"
          v-bind:event="event" />
      </div>
    
  <!-- </div> -->
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
      
    },
 
  }
</script>

<style scoped>
.event-grid {
  display: flex;
  flex-wrap: wrap;
  margin: -1rem; /* Adjust as needed for spacing between event boxes */
  padding: 2rem;
}

.hero.has-background-image {
  background-image: url('https://cdnassets.hw.net/41/fd/6531e2544a668d89d3211d785407/washu-east-end-transformation-1.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  position: relative;
  padding-top: 2rem; /* Adjust the padding as needed */
}
.highlighted-title {
  background-color: rgb(1, 166, 255); /* Adjust the color and transparency as needed */
  padding: 0.2rem 0.4rem; /* Add padding for space between the text and highlight */
  border-radius: 3px; /* Add border-radius for rounded corners; adjust as needed */
}

.hero.has-background-image::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.1) !important; /* Adjust the transparency by changing the last value */
  z-index: -1;
}


</style>