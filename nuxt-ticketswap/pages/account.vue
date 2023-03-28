
<template>
  <div class="account">
    <h1>Welcome to your account page.</h1>

    <div class="column is-12">
      <button @click="logout()" class="button is-danger">Log out</button>
    </div>

    <div class="column is-12">
      <h2 class="subtitle">Your tickets!</h2>


    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        tickets: []
      }
    },
    mounted() {
      this.getTickets()
    },
    methods: {
      logout() {
            localStorage.removeItem("token")
            this.$store.commit('deauthenticateUser')
            this.$router.push('/')
            this.$store.commit('emptyCart')
        },
        async getTickets() {
          await $fetch('/api/v1/tickets', { method: "GET" })
          .then(response => {
            this.tickets = response
          })
          .catch(error => {
            console.log(error)
          })
        }
    }
  }
</script>