from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum


# Create your views here.
from django.views.generic import ListView, DetailView

from invoice.models import Invoice, DetailInvoice
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
        return Invoice.objects.filter(loan=loan)


class InvoiceDetail(DetailView):
    model = Invoice
    template_name = 'invoice/card.html'

    def get_object(self):
        return get_object_or_404(Invoice, id=self.kwargs['invoice_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice = get_object_or_404(Invoice, id=self.kwargs['invoice_id'])
        context['percentage'] = round((invoice.tax*100)/invoice.subtotal, 2)
        context['invoice_details'] = DetailInvoice.objects.filter(invoice=self.kwargs['invoice_id'])
        return context
