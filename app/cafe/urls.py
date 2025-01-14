from django.urls import path
from cafe import views


app_name = 'cafe'

urlpatterns = [
    path('', views.index_page, name='home'),
    path('orders/', views.orders_list, name='orders-list'),
    path('orders/create/', views.create_order, name='order-create'),
]