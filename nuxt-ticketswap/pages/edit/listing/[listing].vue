<template>
<div class="column is-12 box">
    <h2 class="title">Edit Listing</h2>
        <form class="mt-3" @submit.prevent="enterForm">
            <div class="field">
                <label>Update Price ($)</label>
                <div class="control">
                    <input type="number" class="input" v-model="price">
                </div>
            </div>

            <div class="error-notification" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <button class="button is-dark" @click="enterForm">Submit</button>
            <button @click="$router.push('/my-listings')" class="button ml-4">Back</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'EditListing',
    data() {
        return {
            price: null,
            errors: []
        }
    },
}


</script>