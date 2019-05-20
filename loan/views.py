from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import json

# Create your views here.
from invoice.models import Invoice
from loan.forms import LoanForm
from loan.models import PaymentPeriod, Loan


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


