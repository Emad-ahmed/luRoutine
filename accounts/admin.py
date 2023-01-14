from django.contrib import admin
from .models import BindAccount


@admin.register(BindAccount)
class BindAccountAdmin(admin.ModelAdmin):
    pass
