from django.contrib import admin
from .models import Semester, CourseOffered, CourseDistribution, DistributedSectionDetail
from import_export.admin import ImportExportModelAdmin

@admin.register(Semester)
class SemesterAdmin(ImportExportModelAdmin):
    pass



@admin.register(CourseOffered)
class CourseAdmin(ImportExportModelAdmin):
    pass



@admin.register(CourseDistribution)
class CourseDistributionAdmin(ImportExportModelAdmin):
    pass


@admin.register(DistributedSectionDetail)
class MergedSectionDetailsAdmin(ImportExportModelAdmin):
    pass
