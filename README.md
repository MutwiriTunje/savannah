# Simple Customer Order Service

## Overview
This is a simple service that manages customers and orders with SMS notifications using Africa's Talking API. It also uses Auth0/OpenID for authentication and authorization.

## Technologies Used
- Django Rest Framework
- OpenID Connect (Auth0)
- Africa's Talking API for SMS
- GitHub Actions for CI/CD

## Setup Instructions

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. create an .env file 
4. Replace these;AFRICAS_API_KEY, AFRICAS_USERNAME, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_DOMAIN with your own credentials
5. Run migrations using `python manage.py migrate`.
6. Start the server using `python manage.py runserver`.
7. Create a superuser using `python manage.py createsuperuser`.
8. Set up Africa’s Talking SMS gateway for notifications.

## Running Tests
Run tests using the command `coverage run manage.py test` and check the coverage report using `coverage report`.



