<template>
  <div id="wrapper">
   
    <nav class="navbar ">
  <div class="navbar-brand">
     <router-link to="/" class="navbar-item"><strong>TicketSwap</strong></router-link>

  </div>

  <div id="navMenubd-example" class="navbar-menu is-active">
    <div class="navbar-start">
      <router-link to="/seller" class="navbar-item">Create New Event</router-link>

      <router-link to="/about" class="navbar-item">About</router-link>
    </div>

    <div class="navbar-end">
    
      <div class="navbar-item">
        <div class="field is-grouped">

          <template v-if="$store.state.isAuthenticated">
            <p class="control">
              <span>
                <button class="bd-tw-button button" @click="$router.push('/tickets')">My Tickets</button>
              </span>
            </p>


            <p class="control">
              <span>
                <button class="bd-tw-button button" @click="$router.push('/account')">Account</button>
              </span>
            </p>

            <p class="control">
  
                  <button class="button is-info " @click="$router.push('/cart')">Cart</button>
            </p>

          </template>

          <template v-else>
            <p class="control">
                  <button class="button is-info" @click="$router.push('/signup')">Signup</button>
                
            </p>

            <p class="control">
                <div>
                  <button class="button is-info" @click="$router.push('/login')">Login</button>
                </div>
            </p>
          </template>
        </div>
      </div>
    </div>
  </div>
</nav>
    

    <section class="section">
      <router-view/>
    </section>


    

  </div>
</template>

<script>

export default {
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  beforeRouteLeave(to, from, next) {
    this.$parent.$el.querySelector("router-view").classList.add("has-padding");
    next();
  }
}
</script>

<style scoped>
router-view:not(.no-padding) {
  padding: 1rem; /* Adjust the padding value as needed */
}
</style>
