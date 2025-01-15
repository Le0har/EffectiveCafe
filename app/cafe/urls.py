from django.urls import path
from cafe import views


app_name = 'cafe'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('orders/', views.order_list, name='order-list'),
    path('orders/create/', views.create_order, name='order-create'),
]