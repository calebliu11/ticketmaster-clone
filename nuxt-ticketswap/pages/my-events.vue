<template>
    <h2 class="title">My Events</h2>
        <div class="events-list column is-size-4 is-centered">
            <ul v-for="event in events">
                <div v-if="dateInPast(event)" class="box mt-5 has-background-grey-lighter">  
                    <div class="content">
                        <p>
                            <strong class="is-size-4 has-text-weight-semibold">{{ event.name }}</strong>
                            <br>
                            <span class="is-size-5">{{ computeFormattedDate(event.date) }}</span>
                            <br>
                            <span class="is-size-5 has-text-info">{{ event.description }}</span>
                            <br>
                            <span class="is-size-5 has-text-weight-semibold">PAST</span>
                        </p>
                    </div>   
                </div>

                <div v-else class="box mt-4">  
                    <div class="content">
                        <p>
                            <strong class="is-size-4 has-text-weight-semibold">{{ event.name }}</strong>
                            <br>
                            <span class="is-size-5">{{ computeFormattedDate(event.date) }}</span>
                            <br>
                            <span class="is-size-5 has-text-info">{{ event.description }}</span>
                            <br>
                            <span class="is-size-5 has-text-weight-semibold">{{ event.status }}</span>
                        </p>
            
                        <div class="buttons">
                            <nuxt-link class="button is-success" :to="`/edit/event/${event.slug}`">Edit Event</nuxt-link>
                        </div>
                    </div>   
                </div>

            </ul>
        </div>
</template>

<script>
import { toast } from 'bulma-toast'

export default {
    data() {
        return {
            events: []
        }
    },
    mounted() {
        document.title = 'Ticketswap | My Events'
        this.getEvents()
    },
    methods: {
        async getEvents() {
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
            await $fetch("api/v1/events/", { method: "GET", headers })
            .then((response) => {
                this.events = response
                console.log(JSON.stringify(this.events))
            })
            .catch((error) => console.error(error))
        },
        computeFormattedDate(unformatted_date) {
            const date = new Date(unformatted_date);
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return date.toLocaleDateString('en-US', options);
        },
        dateInPast(event){
            const eventDate = new Date(event.date)
            eventDate.setHours(eventDate.getHours() + 29) 
            return eventDate < new Date()
        }
    }
}
</script>