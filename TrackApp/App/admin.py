from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company']
    search_fields = ['name', 'company']


@admin.register(Device)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'condition']
    search_fields = ['name']


@admin.register(DeviceLog)
class DeviceLogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'device', 'check_in_time', 'check_out_time', 'check_in_condition', 'check_out_condition']
    search_fields = ['employee', 'device']
    list_filter = ['employee', 'device']
