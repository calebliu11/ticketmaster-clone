
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
      logout() {
            localStorage.removeItem("token")
            this.$store.commit('deauthenticateUser')
            this.$router.push('/')
            this.$store.commit('emptyCart')
        },
    }
  }
</script>