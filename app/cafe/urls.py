from django.urls import path
from cafe import views


app_name = 'cafe'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('orders/', views.order_list, name='order-list'),
    path('orders/create/', views.order_create, name='order-create'),
    path('orders/find/', views.order_find, name='order-find'),
    path('orders/<int:order_id>', views.order_detail, name='order-detail'),
    
]