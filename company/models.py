from django.db import models
from django.conf import settings


def custom_company_upload_to(instance, filename):
    try:
        old_instance = Company.objects.get(pk=instance.pk)
    except Company.DoesNotExist:
        old_instance = None
    if old_instance is not None:
        old_instance.logo.delete()
    return 'companies/%Y/%m/%d/' + filename


class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nombre de la empresa", max_length=40)
    address = models.CharField(verbose_name="Dirección", max_length=200, null=True, blank=True)
    phone = models.CharField(verbose_name="Teléfono", max_length=15, blank=True, null=True)
    city = models.CharField(verbose_name="Ciudad", max_length=20)
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    logo = models.ImageField(upload_to=custom_company_upload_to, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Compañia"
        verbose_name_plural = "Compañias"
        ordering = ['-created']

    def __str__(self):
        return self.name
