from django.shortcuts import redirect, render
from .models import Order
from .forms import OrderForm


def index_page(request):
    return render(request, 'cafe/index.html')


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe:order-list')
    else:
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'cafe/create_order.html', context=context)


def order_list(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'cafe/order_list.html', context=context)