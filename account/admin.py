from django.contrib import admin
from company.models import Company


# Register your models here.
@admin.register(Company)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)
