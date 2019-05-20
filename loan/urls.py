from django.urls import path
from . import views


urlpatterns = [
    # Post views
    path('', views.loan, name='loan'),
    path('list/', views.LoanList.as_view(), name='loan_list'),
    path('create/', views.LoanCreate.as_view(), name='loan_create'),
    path('get_period_value/', views.get_period_value, name='get_period_value'),
]