
<template>
  <div class="account">
    <h1 class="title" v-if="this.user_username==''">Account</h1>
    <h1 v-else class="title">Welcome, {{ this.user_username }}</h1>

    <div class="box">
      <strong class="is-size-4">Seller Dashboard</strong>
      <br>
      <span class="is-size-5">Account Balance: <p v-if="funds" style="display: inline;" class="has-text-weight-semibold is-italic has-text-primary">${{ funds }}</p>
      
      <p v-else style="display: inline;" class="has-text-weight-semibold is-italic has-text-primary">$0</p>
      </span>

      <div class="buttons is-grouped mt-4" >

        <button v-if="this.account_pending" class="button is-link">Account being created...</button>

        <button v-if="this.$store.state.isActive && this.$store.state.accountId != ''" class="button is-info" @click=viewSellerAccount() >View Seller Account</button>

        <button v-if="funds > 0 && this.$store.state.isActive" @click="cashout()" class="button is-primary">Cashout</button>

        <button v-if="!this.$store.state.isActive && !this.account_pending" @click="createSellerAccount()" class="button is-primary">Create Seller Account</button>


      </div>




    </div>

    <div class="box">
      <strong class="is-size-4 mb-4">Events Dashboard</strong>
      <br>


      <button @click="$router.push('/my-listings')" class="button mt-4">View My Listings</button>

      <button @click="$router.push('/my-events')" class="button is-dark ml-4 mt-4">View My Events</button>

      <div class="buttons is-grouped mt-4" >

        <button v-if="reports.length>0" @click="$router.push('/dispute-reports')" class="button is-rounded is-warning">Dispute Reports</button>
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
          account_pending: false,
          user_username: '',
          reports: [],
          errors: [],
      }
  },
  mounted() {
    this.getAccountDetails()
    document.title = 'Ticketswap | Account'
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
          this.account_pending = response['transfers'] == 'pending'
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
      else {
        this.account_pending = false
      }
      
      $fetch("api/v1/reports/", {method: "GET", headers})
      .then((response) => {
        console.log(response)
        this.reports = response
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

      $fetch("api/v1/account/", { method: "GET", headers })
      .then((response) => {
        console.log(response)
        this.funds = response["funds"] 
        this.user_username = response['user_username']
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
          user: 22,
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
        user: 22,
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
                  duration: 3000,
                  position: 'bottom-left',
              })
              console.log(response)
              window.location.reload(true)
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
    },
    viewSellerAccount() {
      window.open("https://dashboard.stripe.com/" + this.$store.state.accountId + "/test/dashboard/", "_blank")
    }
  }
}
</script>