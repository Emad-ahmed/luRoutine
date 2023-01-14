from django.contrib import admin
from .models import Batch, Section


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
