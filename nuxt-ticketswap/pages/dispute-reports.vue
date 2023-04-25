<template>
<div v-if="reports.length==0">
    <strong class="title">You have no reports to dispute!</strong>
</div>
<div v-else>
    <strong class="title mb-3">Dispute Reports</strong>
    <br>
    <span class="is-size-6 is-italic">Note: User reports about your listings will appear here. Please submit evidence if you wish to dispute claims. Disputes will be reviewed by admins.</span>

    <ul v-for="report in reports">
        <div v-if="report.disputed==false" class="box mt-4">  
            <div class="content">
                <strong class="is-size-4 has-text-weight-semibold">{{ report.reason }}</strong>
                <br>
                <span class="has-text-weight-semibold is-italic mb-4">{{ report.description }}</span>
                <br>
                
                <p class="has-text-weight-semibold is-italic">Listing ID: {{ report.listing }}</p>

                <button @click="showDisputeForm(report)" class="button is-danger mb-4">Dispute</button>

                <div id="report-form" v-if="report.show_form">
                    <form @submit.prevent="enterForm(report)">
                        <div hidden>{% csrf_token %}</div>

                        <div class="field">
                            <label>Explanation:</label>
                            <div class="control">
                                <textarea class="textarea" rows="5" cols="50" v-model="explanation" placeholder="Address any claims brought up here." required></textarea>
                            </div>
                        </div>

                        <input type="submit" class="button is-primary" value="Submit">

                        <button @click="cancelDispute(report); " class="button ml-3">Cancel</button>
                    </form>
                </div>
            </div>
        </div>
    </ul>
</div>
</template>

<script>
import { toast } from 'bulma-toast'

export default {
    name: "DisputeReports",
    data() {
        return { 
            reports: [],
            explanation: '',
        }
    },
    mounted() {
        this.getReports()

        document.title = 'Ticketswap | Dispute Reports'

    },
    methods: {
        async getReports() {
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
            $fetch('api/v1/reports/', { method: "GET", headers })
            .then((response) => {
                console.log(response)
                this.reports = response
            })
            .catch(error => {
                if (error.response) {
                    console.log(JSON.stringify(error.response._data))
                }
                else if (error.message) {
                    console.log(JSON.stringify(error.message))
                }
            })
        },
        showDisputeForm(report) {
            report.show_form = !report.show_form
        },
        cancelDispute(report){
            report.show_form = false
        },
        enterForm(report) {
            const formData = {
                user: 22,
                report: report.id, 
                explanation: this.explanation
            }
            
            const headers = { 'Content-Type': 'application/json', 'Authorization': "Token " + this.$store.state.token};
            $fetch('api/v1/disputes/', { method: "POST", headers, body: formData })
            .then((response) => {
                console.log(JSON.stringify(response))
                toast({
                    message: 'Your dispute has been submitted and will be reviewed!',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 1500,
                    position: 'bottom-left',
                })
                report.show_form = false
                this.explanation = ''
                window.location.reload(true)
            })
            .catch(error => {
                if (error.response) {
                    console.log(JSON.stringify(error.response))
                }
                else if (error.message) {
                    console.log(JSON.stringify(error))
                }
            })
            
        }
    }
}
</script>