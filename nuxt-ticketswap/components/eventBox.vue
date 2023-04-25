<template>
    
    <!-- <div class="column is-size-4 is-centered "> -->
    <!-- <div class="event-grid">  -->

        <div v-if="event.status=='CANCELED'" class="box has-background-grey-lighter">  
            <div class="content">
                <p>
                    <strong class="has-text-danger is-italic">{{ event.status }}</strong>
                    <br>
                    <strong class="is-size-4 has-text-weight-semibold">{{ event.name }}</strong>
                    <br>
                    <span class="is-size-5">{{ formattedDate }}</span>
                    <br>
                    <span class="is-size-5 has-text-info">{{ event.description }}</span>
                </p>
            </div>    
        </div>

        <div v-else class="box">  
            <div class="content">
                <p>
                    <strong class="is-size-4 has-text-weight-semibold">{{ event.name }}</strong>
                    <br>
                    <span class="is-size-5">{{ formattedDate }}</span>
                    <br>
                    <span class="is-size-5 has-text-info">{{ event.description }}</span>
                </p>
            </div>    
            
            <template v-if="$store.state.isAuthenticated">
                <div class="buttons">
                    <nuxt-link class="button is-success is-normal" :to="`/listings/${event.slug}`">View Tickets</nuxt-link>

                    <nuxt-link class="button is-warning is-normal" :to="`/listings/sell/${event.slug}`">Sell Ticket</nuxt-link>
                </div>
            </template>
            <template v-else="$store.state.isAuthenticated">
                <div class="buttons">
                    <nuxt-link class="button is-success is-normal" :to="'/login'">Login To View Tickets</nuxt-link>

                </div>
            </template>
        </div>
    <!-- </div> -->
</template>




<script>
export default {
    name: 'eventBox',
    props: {
        event: Object
    }, 
    computed: {
    formattedDate() {
        const date = new Date(this.event.date);
        const currentTimeZoneOffset = date.getTimezoneOffset();

        const targetTimeZoneOffset = 800; 
        const timeDifferenceInMinutes = targetTimeZoneOffset - currentTimeZoneOffset;
        const newDate = new Date(date.getTime() + (timeDifferenceInMinutes * 60 * 1000));


        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return newDate.toLocaleDateString('en-US', options);
    }
  }
    
}
</script>


<style scoped>


.box {
  flex: 0 0 calc(33.333% - 2rem); /* 33.333% for 3 columns, 2rem for spacing between event boxes */
  margin: 1rem; /* Adjust as needed for spacing between event boxes */
  /* Add other required styles for the event box */
}
</style>
