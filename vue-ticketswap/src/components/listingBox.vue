<template>
    <div class="column is-size-4 is-centered ">
        <div class="box ">
        
        
            <h3 class="is-size-4 has-text-weight-semibold">{{ listing.event }}</h3>
            <p class="is-size-6">{{ listing.description }}</p>

            <p class="is-size-6 has-text-success">${{ listing.price }}</p>
                   
                    

               
           
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