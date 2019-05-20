from django.urls import path
from . import views


urlpatterns = [
    # Post views
    path('', views.loan, name='loan'),
    path('get_period_value/', views.get_period_value, name='get_period_value'),
]