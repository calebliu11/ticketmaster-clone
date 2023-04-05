
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
        <button @click="cashout()" class="button is-primary">Cashout</button>

        <button @click="$router.push('/my-listings')" class="button">View My Listings</button>
      </div>
    </div>

    <div class="account-form">
      <form @submit.prevent="editAccountDetails">
        <div hidden>{% csrf_token %}</div>

        <div class="field">
            <label>Account Number</label>
            <div class="control">
                <input type="number" class="input" v-model="account_number">
            </div>
        </div>

        <div class="field">
            <label>Routing Number</label>
            <div class="control">
                <input type="number" class="input" v-model="routing_number">
            </div>
        </div>

        <div class="error-notification" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <div class="field">
            <div class="control">
                <button>Submit</button>
            </div>
        </div>
      </form>

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

        this.$router.push('/')
    },
    async getAccountDetails() {
      const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
      await $fetch("api/v1/account/", { method: "GET", headers })
      .then((response) => {
        this.funds = response["funds"]
      })
      .catch((error) => console.error(error))
    },
    editAccountDetails(){
      this.errors = []

      if (this.account_number === '') {
          this.errors.push('First name is required!')
      }

      if (this.routing_number === '') {
          this.errors.push('Last name is required!')
      }

      console.log(typeof(this.funds))

      if (!this.errors.length) {
        const formData = {
          user: 8,
          funds: parseFloat(this.funds),
          account_number: this.account_number,
          routing_number: this.routing_number,
        }

        const csrftoken = Cookies.get('csrftoken');
        const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token, 'X-CSRFToken': csrftoken};

        $fetch("api/v1/account/", { method: "POST", headers, body: formData} )
          .then(() => {
              toast({
                  message: 'Your account details were updated!',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 1000,
                  position: 'bottom-left',
              })
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
    },
  }
}
</script>