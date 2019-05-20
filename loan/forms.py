from django import forms

from customer.models import Customer
from loan.models import PaymentPeriod, Loan


class LoanForm(forms.Form):
    cost = forms.DecimalField(label="Costo")
    initial_fee = forms.DecimalField()
    taxes = forms.DecimalField()
    total_periods = forms.IntegerField()
    payment_period = forms.ModelChoiceField(queryset=PaymentPeriod.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control form-control-alternative'}
    ), empty_label="Seleccione un periodo de pago")


class LoanCreateForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('customer', 'cost', 'initial_fee', 'taxes', 'total_periods', 'date', 'payment_period')
        widgets = {
            'customer': forms.Select(attrs={'class':'form-control form-control-alternative'}),
            'cost': forms.NumberInput(attrs={'class':'form-control form-control-alternative'}),
            'initial_fee': forms.NumberInput(attrs={'class':'form-control form-control-alternative'}),
            'taxes': forms.NumberInput(attrs={'class':'form-control form-control-alternative'}),
            'total_periods': forms.NumberInput(attrs={'class':'form-control form-control-alternative'}),
            'date': forms.SelectDateWidget(attrs={'class':'form-control form-control-alternative'}),
            'payment_period': forms.Select(attrs={'class':'form-control form-control-alternative'}),
        }

    def __init__(self, *args, **kwargs):
        super(LoanCreateForm, self).__init__(*args, **kwargs)
        self.fields['payment_period'].empty_label = "Seleccione el periodo de pago"
        self.fields['customer'].empty_label = "Seleccione un cliente"
