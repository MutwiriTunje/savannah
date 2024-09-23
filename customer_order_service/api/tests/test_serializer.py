from django.test import TestCase
from ..models import Customer, Order
from ..serializer import CustomerSerializer, OrderSerializer

class CustomerSerializerTest(TestCase):
    def setUp(self):
        # Create a sample customer for testing
        self.customer_data = {
            'name': 'John Paul',
            'code': 'MP',
            'phone_number': '1234567890',
        }
        self.serializer = CustomerSerializer(data=self.customer_data)


    def test_serializer_representation(self):
        customer = Customer.objects.create(**self.customer_data)
        serialized_data = CustomerSerializer(customer).data
        self.assertEqual(serialized_data['name'], 'John Paul')
    




class OrderSerializerTest(TestCase):
    def setUp(self):
        # Create a sample customer
        self.customer = Customer.objects.create(
            name='Kiraitu Murungi',
            code='governor',
            phone_number='9876543210',
        )
        # Create a sample order
        self.order_data = {
            'customer': self.customer,
            'item': 'cement',
            'amount': 850,
        }
        self.serializer = OrderSerializer(data=self.order_data)

    
    def test_serializer_representation(self):
        order = Order.objects.create(**self.order_data)
        serialized_data = OrderSerializer(order).data
        self.assertEqual(serialized_data['item'], 'cement')
        
