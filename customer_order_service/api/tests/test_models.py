from django.test import TestCase
from ..models import Customer, Order

class CustomerModelTest(TestCase):
    def test_customer_str_representation(self):
        customer = Customer.objects.create(
            name='Sir Lancelot',
            code='KNIGHT123',
            phone_number='1234567890',
        )
        self.assertEqual(str(customer), 'Sir Lancelot')
        # Add more assertions for other fields as needed

class OrderModelTest(TestCase):
    def setUp(self):
        # Create a sample customer
        self.customer = Customer.objects.create(
            name='King Arthur',
            code='EXCALIBUR',
            phone_number='9876543210',
        )
        # Create a sample order
        self.order = Order.objects.create(
            customer=self.customer,
            item='Holy Grail',
            amount=42.0,
        )

    def test_order_str_representation(self):
        self.assertEqual(
            str(self.order),
            f"Order for {self.customer}: Holy Grail"
        )
        # Add more assertions for other fields as needed
