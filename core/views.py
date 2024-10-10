from decimal import Context
from typing import Self
from urllib import request
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import context
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DetailView
from core.models import Counterparts,Priv,Resume 
from core.forms import KontrForm, ResumeForm
from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView



# Create your views here.
import time

# class contr(request):
#   template_name = 'main.html'
#
#   context={'}
#   return render(request,template_name,context)


class CustomHtmxMixin:
    def dispatch(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        self.template_htmx = self.template_name
        if not self.request.META.get("HTTP_HX_REQUEST"):
            self.template_name = "components/include_block.html"
        else:
            time.sleep(1)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["template_htmx"] = self.template_htmx
        return super().get_context_data(**kwargs)


class Home(TemplateView):
    template_name = "home.html"


class Company(CustomHtmxMixin, TemplateView):
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = self.kwargs["company_slug"]
        # kwargs['hyu'] = Counterparts.objects.filter(slug=self.)
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["company_slug"]

        context["huy"] = Counterparts.objects.get(slug=slug)
        context["form"] = KontrForm()

        return context

    def post(self, request, *args, **kwargs):

        slug = self.kwargs["company_slug"]

        self.object = Counterparts.objects.get(slug=slug)
        return super().post(request, *args, **kwargs)


class CreateCompany(CustomHtmxMixin, TemplateView):
    template_name = "create_company.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Створити компанію"
        context = super().get_context_data(**kwargs)
        context["form"] = KontrForm()

        return context

    def post(self, request, *args, **kwargs):
        form = KontrForm(data=request.POST)
        # slug = self.kwargs["company_slug"]
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:main'))
        else:
            return HttpResponse(form.errors.values())
   

class CreateUser(CustomHtmxMixin, TemplateView):
    template_name = "create_user.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Створити користувача"
        return super().get_context_data(**kwargs)


class Login(TemplateView):
    template_name = "login.html"


class Main(CustomHtmxMixin, TemplateView  ):
    template_name = "main.html"

    def get_context_data(self,**kwargs):
        kwargs["title"] = "Контрагенти"
        # ddd=Priv.objects.filter(us=auth.user_logged_in)
        gr_us=list(Priv.objects.filter(us=self.request.user))
        ttt=[]
        for sss in gr_us:
            gr=sss.grup
            ttt.append(gr)
        
        kwargs["fignua"] =   Counterparts.objects.filter(group__in=ttt)
        
        return super().get_context_data(**kwargs)


class Users(CustomHtmxMixin, TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Всі користувачі"
        return super().get_context_data(**kwargs)
    
class vvid(CustomHtmxMixin, TemplateView):
    template_name = "vvodcoda.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Введіть код доступу"
        # kwargs["fignua"] = Counterparts.objects.all

        return super().get_context_data(**kwargs)
    
    def post(self, request, *args, **kwargs):
        # form = KontrForm(data=request.POST)
        
       
        s=str(request.POST['name1']) 
        contr=Counterparts.objects.get(okpo_cod=s)

        priv=Priv()
        priv.grup=contr.group
        priv.us=request.user
        priv.cod=s
        priv.save()
        
        # else:
        return HttpResponseRedirect(reverse('core:main'))

        


class upload_resume(CustomHtmxMixin, TemplateView):
    template_name = "upload.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "файли"
        
        context = super().get_context_data(**kwargs)
        context["form"] = ResumeForm()
        all_file=Resume.objects.all()
        context["files"] = all_file
    
        return context

    def post(self, request, *args, **kwargs):
        
        form = ResumeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:main'))
        else:
            return HttpResponse(form.errors.values())

class zakaz(CustomHtmxMixin, TemplateView):
    template_name = "zakaz.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "замовлення на роботу"
        
        return super().get_context_data(**kwargs)
    
    def post(self, request, *args, **kwargs):
        
        return HttpResponseRedirect(reverse('core:main'))









       

