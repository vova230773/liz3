from os import replace
from django.db.models import Q
from django.shortcuts import render
from order.forms import OrderForm
from work.models import employees, posting
from django.contrib import messages

def emp(request):

    emp2 = employees.objects.filter(inn=request.user.inn)

    if emp2.exists():

        emp = employees.objects.get(inn=request.user.inn)

        pos = posting.objects.filter(Q(sub1dt=emp.guid) | Q(sub1kt=emp.guid))

        context = {
          "emp": emp,
          "iii": request.user.inn,
          "emp1": emp.firma.replace("<br->", "\n"),
          "info": emp.info.replace("<br->", "\n"),
          "info2": emp.info2.replace("<br->", "\n"),
          "info3": emp.info3.replace("<br->", "\n"),
          "info4": emp.info4.replace("<br->", "\n"),
          "pos": pos,}
        return render(request, "empcart.html",context=context)
    else:
        messages.success(
                request,
                f"Працівник не зареєстрований у системі.Зверніться до роботодавця",
             )
        context = {
             "title": "Оформлення замовлення на послугу",
             "form": OrderForm(),
             }
        return render(request, "index.html", context=context)
