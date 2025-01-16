from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from .models import Order, OrderItem
from .forms import OrderForm, OrderEditForm


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
        context = {
            'order': order,
        }
        return render(request, 'cafe/order_detail.html', context)


def order_find(request): 
    if request.method == 'POST':
        context = {
        'orders': Order.objects.all(),
        }
        data_form = request.POST
        print('data_form', data_form)
        return render(request, 'cafe/order_list.html', context)
    return render(request, 'cafe/order_find.html')


def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        data_form = request.POST
        order.status = data_form['status']
        order.save()
        return redirect('cafe:order-list')
    else:
        form = OrderEditForm(instance=order)
    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'cafe/order_edit.html', context)


def order_delete(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        order.delete()
    return redirect('cafe:order-list')
