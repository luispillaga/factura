from django.urls import path
from . import views


urlpatterns = [
    # Post views
    path('', views.home, name='home'),
]