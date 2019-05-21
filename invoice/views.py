from django.http import Http404
from django.shortcuts import render
from django.db.models import Sum


# Create your views here.
from django.views.generic import ListView

from invoice.models import Invoice
from loan.models import Loan


def home(request):
    return render(request, 'invoice/home.html')


class InvoiceList(ListView):
    model = Invoice
    template_name = 'invoice/invoice_list.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        try:
            loan = Loan.objects.get(pk=self.kwargs['id'])
        except Loan.DoesNotExist:
            raise Http404("El préstamo no existe")
        return Invoice.objects.filter(company=self.request.user.company, loan=loan)

