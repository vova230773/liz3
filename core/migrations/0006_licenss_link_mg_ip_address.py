# Generated by Django 4.2.7 on 2025-03-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_mg_options_alter_mg_mg'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenss',
            name='link',
            field=models.URLField(default=1, max_length=500, verbose_name='посилання на акт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mg',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
