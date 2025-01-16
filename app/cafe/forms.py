from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items']
        widgets = {
            'items': forms.CheckboxSelectMultiple() 
        }


class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']


class SearchForm(forms.Form):
    search_query = forms.IntegerField(label='Введите номер стола')

