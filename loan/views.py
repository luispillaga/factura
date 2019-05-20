from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from loan.forms import LoanForm, LoanCreateForm
from loan.models import PaymentPeriod, Loan
from django.views.generic import CreateView, ListView


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
            loan = form.save(commit=False)
            period = cd['total_periods']
            # for i in period:
                # new_invoice =
            return HttpResponseRedirect(self.get_success_url())


    # if request.method == 'POST':
    #     form = LoanCreateForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         loan = form.save(commit=False)
    #         user = authenticate(request,
    #                             username=cd['username'],
    #                             password=cd['password'])
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponse('Autenticado')
    #             else:
    #                 return HttpResponse('Disable')
    #         else:
    #             return HttpResponse('Invalid login')
    # else:
    #     form = LoanCreateForm()
    # return render(request, 'loan/create_loan.html', {'loan_form': form})
