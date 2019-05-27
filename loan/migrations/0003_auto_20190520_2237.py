# Generated by Django 2.2.1 on 2019-05-21 03:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_auto_20190519_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de compra'),
        ),
    ]