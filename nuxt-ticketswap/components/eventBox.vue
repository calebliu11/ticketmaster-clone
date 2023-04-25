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
                    <strong class="is-size-8 has-text-weight-semibold">
                        <p :class="categoryClass(event.category)">
                            {{ event.category }}
                        </p>
                    </strong>
                    
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
  }, 
  methods: {
    categoryClass(category) {
      switch (category) {
        case "Concert":
          return "text-Concert";
        case "Performance":
          return "text-Performance";
        case "Bar":
          return "text-Bar";
        case "Sports":
          return "text-Sports";
        case "Student Group":
          return "text-Student";
        case "Other":
          return "text-default";
        default:
          return "text-default";
      }
    },
  },
    
}
</script>


<style scoped>
.text-Concert {
  color: rgb(45, 162, 13); /* Change to desired color for category1 */
}
.text-Performance {
  color: rgb(166, 27, 236); /* Change to desired color for category2 */
}
.text-Sports {
  color: rgb(237, 0, 8); /* Change to desired color for category2 */
}
.text-Bar {
  color: rgb(248, 187, 5); /* Change to desired color for category2 */
}
.text-Student {
  color: rgb(234, 255, 7); /* Change to desired color for category2 */
}
.text-default {
  color: #000; /* Change to desired default color */
}


.box {
  flex: 0 0 calc(33.333% - 2rem); /* 33.333% for 3 columns, 2rem for spacing between event boxes */
  margin: 1rem; /* Adjust as needed for spacing between event boxes */
  /* Add other required styles for the event box */
}
</style>
