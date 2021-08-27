from django.contrib import admin
from .models import Hospital, Salesperson


class HospitalModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'hospital', 'mobile']

class SalespersonModelAdmin(admin.ModelAdmin):
    list_display = ['id','sales','hospital']

admin.site.register(Hospital,HospitalModelAdmin)
admin.site.register(Salesperson,SalespersonModelAdmin)