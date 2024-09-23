from rest_framework import serializers
from . models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    phone_number = serializers.CharField(source='customer.phone_number', read_only=True)
    class Meta:
        model = Order 
        fields = ['customer','phone_number','item', 'amount', 'time']



