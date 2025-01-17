from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from cafe.models import Order, OrderItem
from cafe.forms import OrderForm


class GetPagesTestCase(TestCase):

    def test_ok_enter_index_page(self):
        res = self.client.get(reverse('cafe:index'))
        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(res, 'cafe/index.html')

    def test_ok_enter_order_form(self):
        res = self.client.get(reverse('cafe:order-create'))  
        self.assertEqual(res.status_code, HTTPStatus.OK) 
        self.assertTemplateUsed(res, 'cafe/order_create.html')


class FillFormsTestCase(TestCase):

    def setUp(self):
        item_data = {
            'name': 'Солянка сборная мясная',
            'price': 260.00
        }
        new_item = OrderItem.objects.create(**item_data)
        item_data2 = {
            'name': 'Рассольник',
            'price': 210.00
        }
        new_item2 = OrderItem.objects.create(**item_data2)
        self.order_data = {
            'table_number': 3,
            'items': [new_item.pk, new_item2.pk]
        }

    def test_ok_create_order(self):
        form = OrderForm(data=self.order_data)
        self.assertTrue(form.is_valid())
        res = self.client.post(reverse('cafe:order-create'), self.order_data)
        self.assertEqual(res.status_code, HTTPStatus.FOUND)
        self.assertRedirects(res, reverse('cafe:order-list')) 
        self.assertTrue(Order.objects.filter(table_number=self.order_data['table_number']).exists()) 
