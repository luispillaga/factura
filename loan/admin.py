from django.contrib import admin

# Register your models here.
from loan.models import PaymentPeriod, Loan


@admin.register(PaymentPeriod)
class PaymentPeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'cost', 'initial_fee', 'taxes', 'date', 'expiration_date', 'payment_period', 'status')
