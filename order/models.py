from django.db import models

from core.models import Counterparts

class Order(models.Model):
    job_description = models.TextField(null=True, blank=True, verbose_name="Опис роботи")
    create_at = models.DateTimeField(blank=True,auto_now_add=True, verbose_name='Дата створення')
    okpo=models.CharField(max_length=10, verbose_name='okpo')
    contragent = models.CharField(max_length=500, verbose_name='назва контрагента')
    conclusion = models.TextField(null=True, blank=True, verbose_name="Повідомлення виконавця")
    status=models.CharField(max_length=10, verbose_name='статус')
    file = models.FileField(upload_to= 'files/',null=True)
   
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    suma=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сума")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата виконання")
    guid = models.CharField(max_length=99,unique=True, verbose_name='guid')

    class Meta:
        db_table = "Order"
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення № {self.pk} | Замовник {self.contragent} "

