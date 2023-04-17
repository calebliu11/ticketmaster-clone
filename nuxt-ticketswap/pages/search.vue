<template>
    <div class="search-page">
        <div class="columns is-multiline">
            <div class="column is-10">
                <h2 class="title">Search: "{{ query }}"</h2>
            </div>
        </div>

        <template v-if="events.length > 0">
            <eventBox 
                v-for="event in events"
                v-bind:key="event.id"
                v-bind:event="event" />
        </template>
        <template v-else>
            <h2 class="subtitle">
                No listings found for your query!
            </h2>
        </template>
    </div>
</template>

<script>
import eventBox from '@/components/eventBox'

export default {
    name: 'Search',
    
    data() {
        return {
            events: [],
            query: '',
        }
    },
    components: {
      eventBox
    },
    mounted() {
        let url = window.location.search.substring(1)
        let params = new URLSearchParams(url)

        if (params.get('query')) {
            this.query = params.get('query')

            this.doSearch()
        }
    },
    methods: {
        async doSearch() {
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token };
            await $fetch('/api/v1/search/', { method: "POST", headers, body: { 'query': this.query } })
            .then((response) => {
                this.events = response
                console.log(events)
            })
            .catch((error) => console.error(error))
        },
        formattedDate(listing) {
            const date = new Date(listing.date);
            const currentTimeZoneOffset = date.getTimezoneOffset();

            const targetTimeZoneOffset = 800; 
            const timeDifferenceInMinutes = targetTimeZoneOffset - currentTimeZoneOffset;
            const newDate = new Date(date.getTime() + (timeDifferenceInMinutes * 60 * 1000));


            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return newDate.toLocaleDateString('en-US', options);
        },
    }
}
</script>