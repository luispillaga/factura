# Generated by Django 2.2.1 on 2019-05-23 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20190521_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='company',
        ),
    ]
