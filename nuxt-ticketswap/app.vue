<template>
  <div id="wrapper">
   
    <nav class="navbar ">
  <div class="navbar-brand">
     <router-link to="/" class="navbar-item"><strong>TicketSwap</strong></router-link>

  </div>

  <div id="navMenubd-example" class="navbar-menu">
    <div class="navbar-start">
     
      
      <router-link to="/seller" class="navbar-item">Sell</router-link>

      <router-link to="/about" class="navbar-item">About</router-link>

    </div>

    <div class="navbar-end">
    
      <div class="navbar-item">
        <div class="field is-grouped">

          <template v-if="$store.state.isAuthenticated">
            <p class="control">
              <a class="bd-tw-button button">
                <span class="icon">

                  <i class="fa-regular fa-user"></i>
                </span>
                <span>
                  <router-link to="/account">My Account</router-link>
                </span>
              </a>
            </p>
          </template>

          <template v-else>
            <p class="control">
              <a class="button is-primary">
                <span class="icon">
                  <i class="fa-solid fa-right-to-bracket"></i>             
                </span>
                <span>
                  <router-link to="/signup">Sign Up</router-link>
                </span>
                
              </a>
            </p>

            <p class="control">
              <a class="button is-primary">
                <span class="icon">
                  <i class="fa-solid fa-right-to-bracket"></i>             
                </span>
                <span>
                  <router-link to="/login">Login</router-link>
                </span>
                
              </a>
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
import axios from 'axios'

export default {
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Auth-Token: " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>