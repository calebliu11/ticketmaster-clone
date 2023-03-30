
<template>
  <div class="account">
    <h1>Welcome to your account page.</h1>

    <div>
      <h2>Your Listings</h2>
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
                      <p class="has-text-weight-semibold is-italic has-text-primary">${{ listing.price }}</p>
                  </p>
              </div>    
            </div>
        </ul>
    </div>
    <div class="column is-12">
      <button @click="logout()" class="button is-danger">Log out</button>
    </div>
  </div>
</template>

<script>
  import listingBox from '@/components/listingBox'

  export default {
    data() {
        return {
            listings: []
        }
    },
    mounted() {
      this.getListings()
    },
    components: {
      listingBox
      
    },
    methods: {
      async logout() {
          const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
          await $fetch("api/v1/token/logout", { method: "POST", headers, body: {} })

          localStorage.removeItem("token")
          this.$store.commit('deauthenticateUser')
          this.$store.commit('emptyCart')

          
          this.$router.push('/')
      },
      async getListings() {
        const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
        await $fetch("api/v1/listings/", { method: "GET", headers })
        .then((response) => {
          this.listings = response
        })
        .catch((error) => console.error(error))
      }
    }
  }
</script>