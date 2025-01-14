from django.shortcuts import redirect, render
from .models import Order
from .forms import OrderForm


def index_page(request):
    return render(request, 'pages/index.html')


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe:orders-list')
    else:
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'pages/create_order.html', context=context)


def orders_list(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'pages/orders_list.html', context=context)