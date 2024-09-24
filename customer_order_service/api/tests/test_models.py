from django.test import TestCase
from ..models import Customer, Order

class CustomerModelTest(TestCase):
    def test_customer_str_representation(self):
        customer = Customer.objects.create(
            name='Morara Kebaso',
            code='Auditor',
            phone_number='1234567890',
        )
        self.assertEqual(str(customer), 'Morara Kebaso')
        # Add more assertions for other fields as needed

class OrderModelTest(TestCase):
    def setUp(self):
        # Create a sample customer
        self.customer = Customer.objects.create(
            name='Edwin Sifuna',
            code='Judge',
            phone_number='9876543210',
        )
        # Create a sample order
        self.order = Order.objects.create(
            customer=self.customer,
            item='The Constitution',
            amount=42.0,
        )

    def test_order_str_representation(self):
        self.assertEqual(
            str(self.order),
            f"Order for {self.customer}: The Constitution"
        )
        # Add more assertions for other fields as needed
