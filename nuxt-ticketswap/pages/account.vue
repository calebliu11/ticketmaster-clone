
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
                      <span class="is-size-5">{{ listing.status }}</span>
                      <br>
                      <p class="has-text-weight-semibold is-italic has-text-primary">${{ listing.price }}</p>
                  </p>
              </div>    
            </div>
        </ul>
    </div>

    <div class="column is-10">
      <h2 class="subtitle">Your Tickets</h2>
        <ul v-for="order in orders">
            <hr>
              <p>Order on {{ order.created_at }}</p>
                <ul v-for="item in order.items">
                  <div class="box">  
                    <div class="content">
                        <p>
                            <strong class="is-size-4 has-text-weight-semibold">{{ item.event }}</strong>
                            <br>
                            <span class="is-size-5">{{ item.date }}</span>
                            <br>
                            <span class="is-size-5">{{ item.description }}</span>
                            <br>
                            <p class="has-text-weight-semibold is-italic has-text-primary">${{ item.price }}</p>

                            <img :src="`/api/v1/${item.image_url}`" alt="My Image" style="height: 300px;">
                            <br>

                            <span class="is-size-5">Sold by {{ item.seller_email }}</span>

                            <div class="column is-10">
                              <button @click="showReportForm(); " class="button is-danger">Report Fraud</button>
                            </div>


                            <div id="report-form" v-if="showForm">
                              <form @submit.prevent="enterForm(item)">
                                <div hidden>{% csrf_token %}</div>

                                <div class="field">
                                    <label>Reason</label>
                                    <div class="control">
                                        <input type="text" class="input" v-model="reason">
                                    </div>
                                </div>

                                <div class="field">
                                    <label>Description</label>
                                    <div class="control">
                                        <input type="text" class="input" v-model="description">
                                    </div>
                                </div>

                                <input type="submit" class="button" value="Submit Report">
                              </form>
                            </div>

                        </p>
                    </div>   
                  </div>  
                </ul> 
          </ul>
    </div>

    <div class="column is-10">
      <button @click="logout()" class="button is-danger">Log out</button>
    </div>

    
  </div>
</template>

<script>
  import listingBox from '@/components/listingBox'
  import Cookies from 'js-cookie'
  import { toast } from 'bulma-toast'

  export default {
    data() {
        return {
            showForm: false,
            formData: {
              reason: '',
              description: '',
            },
            listings: [],
            orders: []
        }
    },
    mounted() {
      this.getListings()
      this.getOrders()
    },
    components: {
      listingBox
      
    },
    methods: {
      showReportForm() {
        this.showForm = true
      },
      async enterForm(item) {
        const csrftoken = Cookies.get('csrftoken');
        const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token, 'X-CSRFToken': csrftoken};
        const formData = {
            user: 8,
            listing: item.listing,
            reason: this.reason,
            description: this.description,
            verified: false
        }

        await $fetch('/api/v1/report/', { method: "POST", headers, body: formData })
        .then((response) => {
          console.log(response)
          toast({
            message: 'Your report was submitted!',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 1500,
            position: 'bottom-left',
          })
          this.showForm = false
        })
        .catch((error) => {
          if (error.response) {
              console.log(JSON.stringify(error.response._data))
          }
          else if (error.message) {
              console.log(JSON.stringify(error))
          }
        })

    },
    async logout() {
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
    },
    async getOrders() {
      const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
      await $fetch("api/v1/orders/", { method: "GET", headers })
      .then((response) => {
        this.orders = response
      })
      .catch((error) => console.error(error))
    }
  }
}
</script>