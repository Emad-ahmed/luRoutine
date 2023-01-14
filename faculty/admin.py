from django.contrib import admin
from .models import Faculty, Department, Teacher, Program, Curriculum, Course, FacultyDean, DepartmentHead
from import_export.admin import ImportExportModelAdmin


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(FacultyDean)
class FacultyDeanAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(DepartmentHead)
class DepartmentHeadAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    pass
