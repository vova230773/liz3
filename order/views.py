from django.shortcuts import render

from order.forms import OrderForm

def order(request):
    context = {
        'title': 'Оформлення замовлення на послугу',
        'form': OrderForm(),
    }
    return render(request, 'orderss.html', context=context)