<template>
    <div class="column is-size-4 is-centered ">
        <div class="box">
        
        
            <p class="is-size-6">{{ listing.user_email }}</p>

            <p class="is-size-2 has-text-success">${{ listing.price }}</p>
            <router-link v-bind:to="listing.get_absolute_url" class="button is-dark mt-4"> Buy Ticket</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ticketBox',
    props: {
        listing: Object
    }
}
</script>

