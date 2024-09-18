This project is straightforward customers and orders database.
It employs django framework and REST API for inputting customer and order details.
Additionally, i have implemented authentication and authorization using OpenID Connect.
When a new order is added, an SMS alert is sent to the customer using Africa’s Talking SMS gateway.
create an .env file 
then replace these;AFRICAS_API_KEY, AFRICAS_USERNAME, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_DOMAIN
with your own credentials
