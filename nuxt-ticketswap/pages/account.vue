
<template>
  <div class="account">
    <h1>Welcome to your account page.</h1>

    <div class="column is-12">
      <button @click="logout()" class="button is-danger">Log out</button>
    </div>
  </div>
</template>

<script>
  export default {
    methods: {
      async logout() {
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
            await $fetch("api/v1/token/logout", { method: "POST", headers, body: {} })

            localStorage.removeItem("token")
            this.$store.commit('deauthenticateUser')
            this.$store.commit('emptyCart')
  
            
            this.$router.push('/')
        },
    }
  }
</script>