# Generated by Django 4.2.7 on 2025-03-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='guid',
            field=models.CharField(default=1, max_length=99, unique=True, verbose_name='guid'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='suma',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Сума'),
            preserve_default=False,
        ),
    ]
