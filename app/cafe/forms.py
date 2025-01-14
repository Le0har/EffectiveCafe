from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']
        widgets = {
            'items': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}) 
        }