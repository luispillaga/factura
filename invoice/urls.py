from django.urls import path
from . import views


urlpatterns = [
    # Post views
    path('', views.home, name='home'),
    path('list/<int:id>/', views.InvoiceList.as_view(), name='invoice_list'),
    path('detail/<int:invoice_id>/', views.InvoiceDetail.as_view(), name='invoice_detail'),
]