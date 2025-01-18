import datetime
from tkinter.messagebox import askokcancel
from django.db import models

class employees(models.Model):

    guid=models.CharField(max_length=99,unique=True)
    inn = models.CharField(max_length=10, unique=True, verbose_name="інн")
    surname=models.CharField(max_length=150,verbose_name='фамілія')
    nameK=models.CharField(max_length=150,verbose_name='імя')
    fatherly=models.CharField(max_length=150,verbose_name='по-батькові')
    name = models.CharField(max_length=500,verbose_name='найменування')
    bankcard = models.CharField(max_length=50,verbose_name='баківська картка')
    firma = models.TextField(verbose_name="Фірма")
    info = models.TextField(verbose_name='Загальне')
    info2 = models.TextField(verbose_name="Контакти")
    info3 = models.TextField(verbose_name="Зарплата")
    info4 = models.TextField(verbose_name="Документи")
    phone_number = models.CharField(max_length=10, blank=True, null=True , verbose_name="telefon")
    email = models.EmailField(max_length=70, blank=True, verbose_name="e-mail")

    class Meta:
        db_table = "employees"
        verbose_name = "Працівники"
        verbose_name_plural = "Працівники"

    def __str__(self):
        return self.name


class posting(models.Model):

    guid = models.CharField(max_length=99, unique=True)
    suma = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ціна')
    quantity = models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Кількість')
    sub1dt = models.CharField(max_length=99, verbose_name="Субконто1 Дт")
    sub1kt = models.CharField(max_length=99, verbose_name="Субконто1 Кт")
    info = models.TextField(verbose_name="Зміст")
    accdt = models.CharField(max_length=8, verbose_name="Рахунок Дт")
    acckt = models.CharField(max_length=8, verbose_name="Рахунок Кт")
    dat = models.CharField(max_length=99, verbose_name="Дата")
    class Meta:
        db_table = "posting"
        verbose_name = "Проводка"
        verbose_name_plural = "Проводка"

    def __str__(self):
        return self.info
