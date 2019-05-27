from django.db import models
from django.utils.timezone import now

from company.models import Company
from loan.models import Loan


def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
        return 'FAC0001'
    invoice_no = last_invoice.code
    invoice_int = int(invoice_no.split('FAC')[-1])
    width = 4
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'FAC' + str(formatted)
    return new_invoice_no


class Invoice(models.Model):
    loan = models.ForeignKey(Loan, verbose_name="Prestamo", on_delete=models.CASCADE)
    code = models.CharField(verbose_name="Código de Factura",
                            max_length=500, default=increment_invoice_number, null=True, blank=True)
    payment_date = models.DateField(verbose_name="Fecha de pago", default=now)
    subtotal = models.DecimalField(verbose_name="Subtotal", max_digits=10, decimal_places=2)
    tax = models.DecimalField(verbose_name="Iva", max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-created']

    def __str__(self):
        return self.loan.customer.name


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
