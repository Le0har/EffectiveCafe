from django.shortcuts import redirect, render
from .models import Order, OrderItem
from .forms import OrderForm


def index_page(request):
    return render(request, 'cafe/index.html')


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe:order-list')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'foods': OrderItem.objects.all(),
    }
    return render(request, 'cafe/order_create.html', context=context)


def order_list(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'cafe/order_list.html', context=context)


def order_detail(request):
    pass


def order_find(request):
    return render(request, 'cafe/order_find.html')
