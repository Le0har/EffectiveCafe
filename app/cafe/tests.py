from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from cafe.models import Order, OrderItem


class GetPagesTestCase(TestCase):

    def test_ok_enter_index_page(self):
        res = self.client.get(reverse('cafe:index'))
        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(res, 'cafe/index.html')

    def test_ok_create_order_form(self):
        res = self.client.get(reverse('cafe:order-create'))  
        self.assertEqual(res.status_code, HTTPStatus.OK) 
        self.assertTemplateUsed(res, 'cafe/order_create.html')

    def test_ok_create_order(self):
        item_data = {
            'name': 'Солянка сборная мясная',
            'price': 260.00
        }
        new_item = OrderItem.objects.create(**item_data)
        item_data = {
            'name': 'Рассольник',
            'price': 210.00
        }
        new_item2 = OrderItem.objects.create(**item_data)
        order_data = {
            'table_number': 3,
            'items': [new_item, new_item2]
        }
        res = self.client.post(reverse('cafe:order-create'), order_data) 
        print(res.__dict__) 
        self.assertEqual(res.status_code, HTTPStatus.FOUND)
        self.assertRedirects(res, reverse('cafe:order-list')) 
        self.assertTrue(Order.objects.filter(table_number=order_data['table_number']).exists()) 
