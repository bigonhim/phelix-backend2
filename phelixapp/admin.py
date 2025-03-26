from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')

class WorkerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'contact_info', 'skills')

class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'contact_info')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(WorkerProfile, WorkerProfileAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(Job)
