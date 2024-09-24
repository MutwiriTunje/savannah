from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch, MagicMock
from django.urls import reverse
from ..models import Customer, Order
from ..serializer import CustomerSerializer, OrderSerializer
from ..views import send_sms
from django.urls import reverse
from rest_framework import status
from ..models import Customer, Order

class CustomerViewSetTestCase(TestCase):


    def test_create_customer(self):
        """
        Test customer creation and redirection after successful creation
        """
        create_data = {
            "name": "Jane Doe",
            "code": "C456",
            "phone_number": "+254712345678"  # Valid phone number format
        }
        url = reverse('customer-list')  
        response = self.client.post(url, create_data)

        # Print response content for debugging
        if response.status_code == 400:
            print(f"Validation errors: {response.data}")

        # Assert the status code is 302 (redirect on success)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

  