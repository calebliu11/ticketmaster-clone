<template>
  <div id="wrapper">
   

    <nav class="navbar ">
  <div class="navbar-brand">
     <router-link to="/" class="navbar-item"><strong>TicketSwap</strong></router-link>

  </div>

  <div id="navMenubd-example" class="navbar-menu">
    <div class="navbar-start">
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link  is-active" href="/documentation/overview/start/">
          My Tickets
        </a>
        <div class="navbar-dropdown ">
          <a class="navbar-item " href="/documentation/overview/start/">
            Upcoming Events
          </a>
          <a class="navbar-item " href="http://bulma.io/documentation/modifiers/syntax/">
            Past Events
          </a>
          

          <a class="navbar-item is-active" href="http://bulma.io/documentation/components/breadcrumb/">
            Tickets Sold
          </a>
  
        </div>
      </div>
      
      <router-link to="/seller" class="navbar-item">Sell</router-link>

      <router-link to="/about" class="navbar-item">About</router-link>

    </div>

    <div class="navbar-end">
    
      <div class="navbar-item">
        <div class="field is-grouped">
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
          <p class="control">
            <a class="button is-primary">
              <span class="icon">
                <i class="fa-solid fa-right-to-bracket"></i>             
              </span>
              <span>Sign Up</span>
            </a>
          </p>
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

<style lang="scss">
@import '../node_modules/bulma';
</style>
