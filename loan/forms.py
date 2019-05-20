from django import forms

from loan.models import PaymentPeriod


class LoanForm(forms.Form):
    cost = forms.DecimalField(label="Costo")
    initial_fee = forms.DecimalField()
    taxes = forms.DecimalField()
    total_periods = forms.IntegerField()
    payment_period = forms.ModelChoiceField(queryset=PaymentPeriod.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control form-control-alternative'}
    ), empty_label="Seleccione un periodo de pago")
