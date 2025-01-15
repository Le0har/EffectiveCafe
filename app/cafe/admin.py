from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_number', 'status', 'created_at']
    list_display_links = ['id', 'table_number']
    ordering = ['-created_at']
    list_editable = ['status']
    search_fields = ['table_number', 'status']
    filter_horizontal = ['items']
    list_per_page = 10


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    ordering = ['name']
    list_per_page = 20
