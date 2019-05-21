from django.db import models
from django.utils.timezone import now

from customer.models import Customer


class PaymentPeriod(models.Model):
    name = models.CharField(verbose_name="Periodo de Pago", max_length=30)
    value = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Periodo de Pago"
        verbose_name_plural = "Periodos de Pago"

    def __str__(self):
        return self.name


class Loan(models.Model):
    STATUS_CHOICES = (
        ('paying', 'Por Pagar'),
        ('cancelled', 'Cancelado'),
    )
    customer = models.ForeignKey(Customer, verbose_name="Cliente", on_delete=models.CASCADE, blank=True, null=True)
    payment_period = models.ForeignKey(PaymentPeriod, verbose_name="Periodo de pago", on_delete=models.PROTECT)
    cost = models.DecimalField(verbose_name="Costo", max_digits=10, decimal_places=2)
    initial_fee = models.DecimalField(verbose_name="Cuota inicial", max_digits=10, decimal_places=2)
    taxes = models.DecimalField(verbose_name="Impuestos", max_digits=10, decimal_places=2)
    total_periods = models.IntegerField(verbose_name="Total periodos")
    date = models.DateField(verbose_name="Fecha de compra", default=now)
    expiration_date = models.DateField(verbose_name="Fecha de vencimiento", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='paying', verbose_name="Estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"
        ordering = ['-created']

    def __str__(self):
        return self.customer.name
