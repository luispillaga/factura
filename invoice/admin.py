from django.contrib import admin

# Register your models here.
from invoice.models import Invoice, DetailInvoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('code', 'company', 'loan', 'payment_date', 'subtotal', 'tax')


@admin.register(DetailInvoice)
class DetailInvoiceAdmin(admin.ModelAdmin):
    list_display = ('description',)

