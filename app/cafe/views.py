from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
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
    return render(request, 'cafe/order_create.html', context)


def order_list(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'cafe/order_list.html', context)


def order_detail(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        context = {
            'error': f'Заказ с ID = {order_id} не найден!'
        }
        return render(request, 'cafe/errors.html', context)
    else:
        form = OrderForm()
        context = {
            'order': order,
            'form': form,
        }
        return render(request, 'cafe/order_detail.html', context)


def order_find(request):
    return render(request, 'cafe/order_find.html')


def order_edit(request):
    pass


def order_delete(request):
    pass
