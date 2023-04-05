<template>
  <div id="wrapper">
   
    <nav class="navbar ">
  <div class="navbar-brand">
     <router-link to="/" class="navbar-item"><strong>TicketSwap</strong></router-link>

  </div>

  <div id="navMenubd-example" class="navbar-menu">
    <div class="navbar-start">
      <router-link to="/seller" class="navbar-item">Create New Event</router-link>

      <router-link to="/about" class="navbar-item">About</router-link>
      <div class="navbar-item">
        <template v-if="$store.state.isAuthenticated">
          <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" placeholder='Search' name="query">
              </div>

              <div class="control">
                <button class="button is-success">
                </button>
              </div>
            </div>
          </form>
        </template>
      </div>
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
                <button class="bd-tw-button button" @click="$router.push('/account')">My Account</button>
              </span>
            </p>

            <p class="control">
  
                  <button class="button is-primary " @click="$router.push('/cart')">Cart</button>
            </p>

          </template>

          <template v-else>
            <p class="control">
                  <button class="button is-primary" @click="$router.push('/signup')">Signup</button>
                
            </p>

            <p class="control">
                <div>
                  <button class="button is-primary" @click="$router.push('/login')">Login</button>
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

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p>
    </footer>
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
  }
}
</script>

