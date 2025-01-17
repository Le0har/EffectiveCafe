from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from .models import Order
from .forms import OrderForm, OrderEditForm, SearchForm


def index_page(request):
    price = Order.objects.filter(status='paid').aggregate(value=Sum('items__price'))
    count = Order.objects.filter(status='paid').count()
    context = {
        'total_price': price,
        'total_count': count,
    }
    return render(request, 'cafe/index.html', context)


def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cafe:order-list')
    context = {
        'form': form,
    }
    return render(request, 'cafe/order_create.html', context)


def order_list(request):
    context = {
        'orders': Order.objects.all().order_by('-created_at'),
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
    form = SearchForm(request.POST or None)
    if form.is_valid():
        value = request.POST['search_query']
        orders = Order.objects.filter(table_number=value)
        context = {
            'orders': orders,
        }
        return render(request, 'cafe/order_list.html', context)
    context = {
        'form': form,
    }
    return render(request, 'cafe/order_find.html', context)


def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = OrderEditForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('cafe:order-list')
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
