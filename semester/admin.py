from django.contrib import admin
from .models import Semester, CourseOffered, CourseDistribution, DistributedSectionDetail


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseOffered)
class CourseOfferedAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseDistribution)
class CourseDistributionAdmin(admin.ModelAdmin):
    pass


@admin.register(DistributedSectionDetail)
class MergedSectionDetailsAdmin(admin.ModelAdmin):
    pass
