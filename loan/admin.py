from django.contrib import admin

# Register your models here.
from loan.models import PaymentPeriod


@admin.register(PaymentPeriod)
class PaymentPeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
