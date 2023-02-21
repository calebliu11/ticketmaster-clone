<template>
    <body>
        <h1>Ticket Posting Form</h1>
        <form action="{% url 'post_ticket' %}" method="post">
        <label for="contact_info">Contact Info:</label><br>
        <textarea id="contact_info" name="contact_info" required placeholder="First Name, Last Name"> </textarea> <br><br>
        <label for="event_name">Event Name:</label> <br>
        <input type="text" id="event_name" name="event_name" required><br><br>
        <label for="venue">Venue Locations:</label><br>
        
        <select id="venue_locations">
            <option value="PBR">PBR</option>
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
        <input type="submit" value="Submit">
        </form>
    </body>
</template>