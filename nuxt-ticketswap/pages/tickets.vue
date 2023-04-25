<template>
    <div v-if="orders.length==0">
        <h2 class="title">My Tickets</h2>
        <strong class="has-text-weight-semibold is-italic">You have no tickets. Purchase some tickets to see them here!</strong>
    </div>
    <div v-else class="column is-10">
        <h2 class="title">My Tickets</h2>
            <ul v-for="order in orders">
                <hr>
                <strong class="is-size-4 has-text-weight-semibold">Order on {{ computeFormattedDate(order.created_at) }}</strong>
                    <ul v-for="item in order.items">
                        <div class="box mt-4">  
                            <div class="content">
                                    <strong class="is-size-4 has-text-weight-semibold">{{ item.event }}</strong>
                                    <br>
                                    <span class="is-size-5">{{ computeFormattedDate(item.date) }}</span>
                                    <br>
                                    <span class="is-size-5 has-text-info">{{ item.description }}</span>
                                    <br>

                                    <p class="has-text-weight-semibold is-italic has-text-primary">${{ item.price }}</p>

                                    <img :src="`/api/v1/${item.image_url}`" alt="My Image" style="height: 300px;">
                                    <br>
                                    <span class="is-size-5">Sold by {{ item.seller_username }}</span>

                                    <div class="column is-10">
                                        <button @click="showReportForm(item); " class="button is-danger">Report Fraud</button>
                                    </div>

                                    
                                    <div id="report-form" v-if="item.show_form">
                                        <form @submit.prevent="enterForm(item)">
                                            <div hidden>{% csrf_token %}</div>

                                            <div class="field">
                                                <label>Reason</label>
                                                <div class="control">
                                                    <input type="text" class="input" v-model="reason">
                                                </div>
                                            </div>

                                            <div class="field">
                                                <label>Description</label>
                                                <div class="control">
                                                    <input type="text" class="input" v-model="description">
                                                </div>
                                            </div>

                                            <input type="submit" class="button is-primary" value="Submit Report">

                                            <button @click="cancelReport(item); " class="button ml-3">Cancel</button>
                                        </form>
                                    </div>
                                </div>   
                        </div>  
                    </ul> 
            </ul>
        </div>
</template>

<script>
import Cookies from 'js-cookie'
import { toast } from 'bulma-toast'

export default {
    data() {
        return {
            formData: {
              reason: '',
              description: '',
            },
            orders: []
        }
    },
    mounted() {
        this.getOrders()
        document.title = 'Ticketswap | My Tickets'
    },
    methods: {
        showReportForm(item) {
            item.show_form = true
        },
        cancelReport(item){
            item.show_form = false
        },
        async enterForm(item) {
            const csrftoken = Cookies.get('csrftoken');
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token, 'X-CSRFToken': csrftoken};
            const formData = {
                user: 22,
                reported_user: item.user,
                listing: item.listing,
                reason: this.reason,
                description: this.description,
                verified: false,
                show_form: false,
                disputed: false,
            }

            await $fetch('/api/v1/report/', { method: "POST", headers, body: formData })
            .then((response) => {
                console.log(response)
                toast({
                    message: 'Your report was submitted!',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 1500,
                    position: 'bottom-left',
                })
                item.show_form = false
                this.reason = ''
                this.description = ''
            })
            .catch((error) => {
                if (error.response) {
                    console.log(JSON.stringify(error.response._data))
                    toast({
                        message: error.response._data.errors,
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2500,
                        position: 'bottom-left',
                })
                item.show_form = false
                this.reason = ''
                this.description = ''
                }
                else if (error.message) {
                    console.log(JSON.stringify(error.message))
                }
             })
        },
        async getOrders() {
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
            await $fetch("/api/v1/orders/", { method: "GET", headers })
            .then((response) => {
                this.orders = response
                console.log(JSON.stringify(this.orders))

            })
            .catch((error) => console.error(error))
        },
        computeFormattedDate(unformatted_date) {
            const date = new Date(unformatted_date);
            const currentTimeZoneOffset = date.getTimezoneOffset();

            const targetTimeZoneOffset = 800; 
            const timeDifferenceInMinutes = targetTimeZoneOffset - currentTimeZoneOffset;
            const newDate = new Date(date.getTime() + (timeDifferenceInMinutes * 60 * 1000));


            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return newDate.toLocaleDateString('en-US', options);
        }
    },
}
</script>