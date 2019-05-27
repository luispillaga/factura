from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from invoice.models import Invoice, DetailInvoice
from loan.forms import LoanForm, LoanCreateForm
from . import forms
from loan.models import PaymentPeriod, Loan
from django.views.generic import CreateView, ListView
from datetime import datetime, date, time, timedelta
import calendar


@login_required
def loan(request):
    loan_form = LoanForm()
    return render(request, 'loan/loan.html', {'loan_form': loan_form})


@login_required
@require_POST
def get_period_value(request):
    payment_period = request.POST['payment_period']
    period = PaymentPeriod.objects.get(id=payment_period)
    value = period.value
    return JsonResponse({'data': value})


class LoanList(ListView):
    model = Loan
    template_name = 'loan/loan_list.html'
    context_object_name = 'loans'

    def get_queryset(self):
        return Loan.objects.filter(company=self.request.user.company)


def get_expiration_date(purchase_date, total_period, period):
    return purchase_date + timedelta(days=((360 / int(period.value)) * total_period))


class LoanCreate(CreateView):
    model = Loan
    template_name = "loan/loan_create.html"
    form_class = LoanCreateForm
    success_url = reverse_lazy('loan_list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = self.get_object

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            my_loan = form.save()
            total_period = cd['total_periods']
            period = cd['payment_period']
            cost = cd['cost']
            initial_fee = cd['initial_fee']
            taxes = cd['taxes']
            debt = (cost-initial_fee)
            my_loan.company = request.user.company
            my_loan.expiration_date = get_expiration_date(cd['date'], total_period, period)
            my_loan.save()
            initial_invoice = Invoice(
                loan=my_loan,
                payment_date=cd['date'],
                subtotal=initial_fee,
                tax=0,
            )
            initial_invoice.save()
            initial_detail_invoice = DetailInvoice(
                invoice=initial_invoice,
                description="Pago inicial",
                value=initial_fee,
            )
            initial_detail_invoice.save()
            for i in range(int(total_period)):
                subtotal = (cost-initial_fee) / total_period
                tax = debt*(taxes/100)*(1/period.value)
                new_invoice = Invoice(
                    loan=my_loan,
                    payment_date=get_expiration_date(cd['date'], i + 1, period),
                    subtotal=subtotal,
                    tax=tax,
                )
                new_invoice.save()
                new_detail_invoice = DetailInvoice(
                    invoice=new_invoice,
                    description="Pago por compra",
                    value=subtotal,
                )
                debt = debt - ((cost-initial_fee) / total_period)
                new_detail_invoice.save()
                new_invoice.save()
            return HttpResponseRedirect(self.get_success_url())
