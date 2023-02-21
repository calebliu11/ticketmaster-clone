<template>
    <body>
        <h1>Ticket Posting Form</h1>
        <form action="{% url 'post_ticket' %}" method="post" id="seller_form">
            <label for="contact_info">Contact Info:</label><br><br>
            <input id="contact_name" name="contact_name" required placeholder= "Name"> <br><br>
            <input id="contact_number" name="contact_number" required placeholder= "Phone Number"> <br><br>
            <input id="contact_email" name="contact_email" required placeholder= "Email"> <br><br>

            <label for="event_name">Event Name:</label> <br>
            <input type="text" id="event_name" name="event_name" required><br><br>
            <label for="venue">Venue Locations:</label><br>
            
            <select id="venue_locations">
                <option value="PBR" id="PBR">PBR</option>
                <option value="handlebar">Handle Bar</option>
                <option value="molly">Molly's</option>
                <option value="tinroof">Tin Roof</option>
                <option value="bpv">Ballpark Village</option>
                <option value="paddy">Paddy O's</option>
            </select><br><br>
            
            <label for="date">Date:</label><br>
            <input type="date" id="date" name="date" required><br><br>
            <label for="ticket_types">Ticket Type:</label><br>
            <!-- Might add more ticket types -->
            <select id="ticket_types">
                <option value="general">General Admission</option>
                <option value="vip">VIP</option>
                <option value="bus">Party Bus</option>
                <option value="other">Other</option>
            </select><br><br>

            <label for="quantity">Quantity:</label><br>
            <input type="number" id="quantity" name="quantity" required><br><br>
            <label for="price">Price:</label><br>
            <input type="number" id="price" name="price" required><br><br>
            <input type="submit" value="Submit" id="button">
        </form>
    </body>
</template>
<style>
    #button{
    background-color: lightblue; 
    color: black; 
    border: 2px solid rgb(12, 61, 175);
    border-radius: 8px;

}

    #button:hover {
    background-color: #4c6daf;
    color: white;
    border-radius: 8px;
}

    body {
    color: rgb(12, 61, 175);
    text-align: center;
    margin: auto;
    width: 50%;
    }

    #seller_form{
    background-color: lightblue;
    text-align: center;
    margin: auto;
    width: 50%;


    }
</style>