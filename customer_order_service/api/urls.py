from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customers', CustomerViewSet.as_view({'post': 'create'}), name="create-customer"),
    path('orders', OrderViewSet.as_view({'post': 'create'}), name="create-order"),
    path('customer-created/', CustomerCreatedView.as_view(), name='customer-created'),
    path('order-success/', OrderSuccessView.as_view(), name='order-success'),
]
