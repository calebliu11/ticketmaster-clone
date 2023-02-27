<template>
    <div class="column is-15">
        <div class="box">
         

            <h3 class="is-size-4">{{ listing.event }}</h3>
            <p class="is-size-6">{{ listing.description }}</p>

            <p class="is-size-6 has-text-grey">${{ listing.price }}</p>

        </div>
    </div>
</template>

<script>
export default {
    name: 'listingBox',
    props: {
        listing: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>