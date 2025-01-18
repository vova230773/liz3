from django.shortcuts import render

from order.forms import OrderForm


def order(request):
    context = {
        "title": "Оформлення замовлення на послугу",
        "form": OrderForm(),
    }
    return render(request, "index.html", context=context)


def podkal(request):
    context = {
        "title": "Оформлення замовлення на послугу",
        "form": OrderForm(),
    }
    return render(request, "podkal.html", context=context)
