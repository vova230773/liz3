# Generated by Django 4.2.7 on 2024-10-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_guid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='suma',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Сума'),
            preserve_default=False,
        ),
    ]
