# Generated by Django 2.2.1 on 2019-05-19 18:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Periodo de Pago')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Periodo de Pago',
                'verbose_name_plural': 'Periodos de Pago',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo')),
                ('initial_fee', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cuota inicial')),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Impuestos')),
                ('total_periods', models.IntegerField(verbose_name='Total periodos')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de préstamo')),
                ('status', models.CharField(choices=[('paying', 'Por Pagar'), ('cancelled', 'Cancelado')], default='finished', max_length=10, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='Cliente')),
                ('payment_period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loan.PaymentPeriod', verbose_name='Periodo de pago')),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
                'ordering': ['-created'],
            },
        ),
    ]