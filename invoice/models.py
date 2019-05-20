from django.db import models
from django.utils.timezone import now

from company.models import Company
from loan.models import Loan


class Invoice(models.Model):
    company = models.ForeignKey(Company, verbose_name="Compañia", on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, verbose_name="Prestamo", on_delete=models.CASCADE)
    code = models.CharField(verbose_name="Código de Factura", max_length=10, unique=True)
    purchase_date = models.DateField(verbose_name="Fecha de comppra", default=now)
    expiration_date = models.DateField(verbose_name="Fecha de comppra", default=now)
    subtotal = models.DecimalField(verbose_name="Subtotal", max_digits=10, decimal_places=2)
    tax = models.DecimalField(verbose_name="Iva", max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-created']

    def __str__(self):
        return self.company.name


class DetailInvoice(models.Model):
    invoice = models.ForeignKey(Invoice, verbose_name="Detalle factura", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Descripción")
    value = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Detalle factura"
        verbose_name_plural = "Detalles factura"
        ordering = ['-created']

    def __str__(self):
        return self.description
