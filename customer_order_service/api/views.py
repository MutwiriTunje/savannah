from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Customer, Order
from .serializer import CustomerSerializer, OrderSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
import africastalking
from django.conf import settings
from rest_framework.response import Response
from django.shortcuts import redirect
from django.views.generic import TemplateView


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
        
    def create(self, request, *args, **kwargs):
        
        # Save the customer 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Redirect to the customer_created.html page
        return redirect('customer-created')
        

    def update(self, request, *args, **kwargs):
        # custom logic for updating a customer
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # custom logic for deleting a customer
        return super().destroy(request, *args, **kwargs)




class CustomerCreatedView(TemplateView):
    template_name = 'customer_created.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data you want to pass to the template
        # For example:
        context['confirmation_message'] = "Customer has been successfully created!"
        return context


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Get the associated customer
        customer = serializer.validated_data['customer']
        phone_number = customer.phone_number 
        customer_name = customer.name

        # Get the ordered item
        ordered_item = serializer.validated_data.get('item', '')        

        # Construct the SMS message
        message = f"Thank you {customer_name} for your order of {ordered_item}!"

        # Now call your send_sms_instance to send the SMS
        send_sms_instance = send_sms()
        send_sms_instance.send(phone_number=phone_number, message=message,)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class send_sms:
    def send(self, phone_number, message):
        username = settings.AFRICAS_USERNAME
        api_key = settings.AFRICAS_API_KEY

        africastalking.initialize(username, api_key)

        # Set your recipients (including the customer's phone number)
        recipients = [phone_number]
        sender = "myShopKe"

        try:
            response = africastalking.SMS.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')
