<template>
    <div class="listings-list">
      <br>
      <h2 class="title">My Listings</h2>
        <ul v-for="listing in listings">
          <div class="box">  
            <div class="content">
                  <p>
                      <strong class="is-size-4 has-text-weight-semibold">{{ listing.event }}</strong>
                      <br>
                      <span class="is-size-5">{{ listing.date }}</span>
                      <br>
                      <span class="is-size-5">{{ listing.description }}</span>
                      <br>
                      <span class="is-size-5 has-text-weight-bold">{{ listing.status }}</span>
                      <br>
                      <p class="has-text-weight-semibold is-italic has-text-primary">${{ listing.price }}</p>
                  </p>
              </div>    
            </div>
        </ul>
    </div>
</template>

<script>
  export default {
    data() {
        return {
            listings: [],
        }
    },
    mounted() {
      this.getListings()
    },
    methods: {
      async getListings() {
        const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
        await $fetch("api/v1/listings/", { method: "GET", headers })
        .then((response) => {
          this.listings = response
        })
        .catch((error) => console.error(error))
      },
  }
}
</script>