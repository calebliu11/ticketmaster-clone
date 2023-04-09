
<template>
  <div class="account">
    <h1 class="title">Account</h1>

    <div class="box">
      <strong class="is-size-4">Dashboard</strong>
      <br>
      <span class="is-size-5">Account Balance: <p v-if="funds" style="display: inline;" class="has-text-weight-semibold is-italic has-text-primary">${{ funds }}</p>
      
      <p v-else style="display: inline;" class="has-text-weight-semibold is-italic has-text-primary">$0</p>
      </span>

      
      <div class="buttons is-grouped mt-4" >

        <button v-if="funds > 0 && this.$store.state.isActive" @click="cashout()" class="button is-primary">Cashout</button>

        <button v-if="!this.$store.state.isActive && this.$store.state.accountId != '' " @click="createSellerAccount()" class="button is-primary">Create Seller Account</button>

        <button @click="$router.push('/my-listings')" class="button">View My Listings</button>
      </div>
    </div>


    <div class="column is-10">
      <button @click="logout()" class="button is-danger">Log out</button>
    </div>

  </div>
</template>

<script>
import Cookies from 'js-cookie'
import { toast } from 'bulma-toast'
export default {
  data() {
      return {
          funds: 0.0,
          errors: [],
      }
  },
  mounted() {
    this.getAccountDetails()
  },
  methods: {
    async logout() {
        localStorage.removeItem("token")
        this.$store.commit('deauthenticateUser')
        this.$store.commit('emptyCart')
        this.$store.commit('activateAccount', false)
        this.$store.commit('setAccountId', '')
        this.$router.push('/')
    },
    getAccountDetails() {
      const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};

      if(!this.$store.state.isActive) {
        $fetch("api/v1/check-transfer/", { method: "GET", headers })
        .then((response) => {
          this.$store.commit('activateAccount', response['transfers'] == 'active')
        })
        .catch(error => {
          if (error.response) {
              this.errors.push(JSON.stringify(error.response._data))
              console.log(JSON.stringify(error.response._data))
          }
          else if (error.message) {
              this.errors.push('Something went wrong. Please try again!')
              console.log(JSON.stringify(error.message))
          }
        })
      }
      
      $fetch("api/v1/account/", { method: "GET", headers })
      .then((response) => {
        console.log(response)
        this.funds = response["funds"]
        this.$store.commit("setAccountId", response['account_id'])
      })
      .catch(error => {
              if (error.response) {
                  this.errors.push(JSON.stringify(error.response._data))
                  console.log(JSON.stringify(error.response._data))
              }
              else if (error.message) {
                  this.errors.push('Something went wrong. Please try again!')
                  console.log(JSON.stringify(error.message))
              }
          })
    },
    async createSellerAccount(){
        const data = {
          user: 8,
          account_id: '',
        }

        const csrftoken = Cookies.get('csrftoken');
        const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token, 'X-CSRFToken': csrftoken};

        $fetch("api/v1/account/", { method: "POST", headers, body: { data }} )
          .then((response) => {
              toast({
                  message: 'Created seller account with Stripe!',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 1000,
                  position: 'bottom-left',
              })
              console.log(response.url)
              window.location = response['url']
          })
          .catch(error => {
              if (error.response) {
                  this.errors.push(JSON.stringify(error.response._data))
                  console.log(JSON.stringify(error.response._data))
              }
              else if (error.message) {
                  this.errors.push('Something went wrong. Please try again!')
                  console.log(JSON.stringify(error.message))
              }
          })
    },
    async cashout() {
      const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
      const cashoutData = {
        user: 8,
        funds: this.funds,
      }

      console.log(cashoutData)

      $fetch("api/v1/cashout/", { method: "POST", headers, body: cashoutData} )
          .then((response) => {
              toast({
                  message: 'Your cashout has been processed!',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 1000,
                  position: 'bottom-left',
              })
              console.log(response)
              this.$router.push('/')
          })
          .catch(error => {
              if (error.response) {
                  this.errors.push(JSON.stringify(error.response._data))
                  console.log(JSON.stringify(error.response))
              }
              else if (error.message) {
                  this.errors.push('Something went wrong. Please try again!')
                  console.log(JSON.stringify(error.message))
              }
          })
    }
  }
}
</script>