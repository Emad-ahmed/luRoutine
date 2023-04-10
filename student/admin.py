from django.contrib import admin
from .models import Batch, Section
from import_export.admin import ImportExportModelAdmin

@admin.register(Batch)
class BatchAdmin(ImportExportModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    pass
