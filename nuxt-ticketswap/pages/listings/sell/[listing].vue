<template>
  <div class="seller-page">  
          <h2 class="title">Sell Ticket</h2>
          <template v-if="$store.state.isAuthenticated">

              <form @submit.prevent="enterForm">
                <div hidden>{% csrf_token %}</div>

                

                <div class="field">
                    <label class="label">Price</label>
                    <div class="control has-icons-left">
                        <input class="input" type="number" v-model="price" >
                        <span class="icon is-small is-left">
                            <font-awesome-icon icon="fa-solid fa-dollar-sign" beat />
                        </span>
                    </div>
                </div>

                <div class="field">
                        <div class="control is-flex">
                            <label class="file-label">
                                <input class="file-input" type="file" @change="onChangeFile" name="image">
                                <span class="file-cta">
                                    <span class="file-icon">
                                        <font-awesome-icon icon="fa-solid fa-upload" />                                    </span>
                                    <span class="file-label" v-if="fileName">
                                        {{ fileName }}
                                    </span>
                                    <span class="file-label" v-else>
                                        Choose a file...
                                    </span>
                                </span>
                            </label>
                        </div>
                </div>

                <div class="error-notification" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="field">
                    <div class="control">
                        <button class="button is-primary" :disabled="isSubmitting">Submit</button>
                    </div>
                </div>
              </form>
          </template>

          <template v-else>
              <h3 class="is-size-4 has-text-weight-semibold">You must be logged in to sell a ticket!</h3>
          </template>
      
  </div>
</template>

<script>
import { toast } from 'bulma-toast'
import Cookies from 'js-cookie'

export default {
  name: 'PostListing',
  data() {
      return {
          user: null,
          user_email: '',
          event: '',
          description: '',
          price: '',
          date: '',
          image: null,
          fileName: '',
          errors: []
          
      }
  },
  mounted() {
      this.getListings()
  },
  methods: {
    async getListings() {
      const slug = this.$route.params.listing
      await $fetch(`/api/v1/listings/${slug}`, { method: "GET" })
        .then((response) => {
          this.ticket = response[0]
          console.log(this.ticket)
        })
        .catch((error) => console.error(error))
    }   ,
  
      onChangeFile(event) {
          const reader = new FileReader();
          reader.readAsDataURL(event.target.files[0]);
          this.fileName = event.target.files[0].name
          reader.onload = () => {
              this.image = reader.result;
          };
      },
      enterForm(){
          this.errors = []
             
              if(this.price < 0) {
                  this.errors.push('Price cannot be negative.')
              }

              if (!this.errors.length) {
                  const formData = {
                      user: 22,
                      user_email: 'seller@wustl.edu',
                      event: this.ticket.event,
                      description: this.ticket.description,
                      price: this.price,
                      date: this.ticket.date,
                      image: this.image,
                  }
                  
                  const csrftoken = Cookies.get('csrftoken');
                  const headers = { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken };

                  $fetch("/api/v1/post-listing/", { method: "POST", headers, body: formData} )
                      .then(() => {
                          toast({
                              message: 'Your listing was created!',
                              type: 'is-success',
                              dismissible: true,
                              pauseOnHover: true,
                              duration: 1000,
                              position: 'bottom-left',
                          })
                          this.$router.push('/')
                      })
                      .catch(error => {
                            if (error.response) {
                                this.errors.push(JSON.stringify(error.response._data))
                                console.log(JSON.stringify(error.response))
                            }
                          else if (error.message) {
                              this.errors.push('Something went wrong. Please try again!')
                              console.log(JSON.stringify(error))
                          }
                      })
              }
      }
  }
}
</script>