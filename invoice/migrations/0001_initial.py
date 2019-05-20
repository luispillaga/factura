# Generated by Django 2.2.1 on 2019-05-19 18:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Código de Factura')),
                ('purchase_date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de comppra')),
                ('expiration_date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de comppra')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Iva')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Compañia')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Loan', verbose_name='Prestamo')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DetailInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice', verbose_name='Detalle factura')),
            ],
            options={
                'verbose_name': 'Detalle factura',
                'verbose_name_plural': 'Detalles factura',
                'ordering': ['-created'],
            },
        ),
    ]