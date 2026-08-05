from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'project_type', 'created_at')
    list_filter = ('project_type',)
    search_fields = ('name', 'phone', 'message')
