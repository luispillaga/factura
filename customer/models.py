from django.db import models


# Create your models here.
class Customer(models.Model):
    id_card = models.CharField(verbose_name="Cédula", unique=True, max_length=10)
    name = models.CharField(verbose_name="Cliente", max_length=50)
    address = models.CharField(verbose_name="Dirección", max_length=50, blank=True, null=True)
    phone = models.CharField(verbose_name="Teléfono", max_length=15)
    city = models.CharField(verbose_name="Ciudad", max_length=20)
    company = models.CharField(verbose_name="Empresa", max_length=30, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created']

    def __str__(self):
        return self.name
