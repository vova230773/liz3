from django.db import models

from core.models import Counterparts

class Order(models.Model):
    guid = models.CharField(max_length=99, unique=True, verbose_name="guid")
    document_type=models.CharField(max_length=99,unique=False, verbose_name='тип документа')
    okpo=models.CharField(max_length=10, verbose_name='okpo')
    contragent = models.CharField(max_length=500, verbose_name='назва контрагента')    
    status=models.CharField(max_length=10, blank=True, verbose_name='статус')
    job_description = models.TextField(null=True, blank=True, verbose_name="Опис роботи")
    conclusion = models.TextField(null=True, blank=True, verbose_name="Повідомлення виконавця")
    file_str = models.CharField(max_length=500, blank=True, verbose_name='урл файлика')    
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    suma=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сума")
    created_timestamp = models.CharField(max_length=10, blank=True, verbose_name="Дата виконання"
    )

    class Meta:
        db_table = "Order"
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення № {self.pk} | Замовник {self.contragent} "
