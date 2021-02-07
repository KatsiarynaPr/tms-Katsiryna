from django.contrib import admin

from applications.KPI.models import KPI


@admin.register(KPI)
class KPIAdminModel(admin.ModelAdmin):
    pass
