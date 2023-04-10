from django.contrib import admin
from .models import Faculty, Department, Teacher, Program, Curriculum, Course, FacultyDean, DepartmentHead
from import_export.admin import ImportExportModelAdmin


@admin.register(Faculty)
class FacultyAdmin(ImportExportModelAdmin):
    pass


@admin.register(FacultyDean)
class FacultyDeanAdmin(ImportExportModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    pass


@admin.register(DepartmentHead)
class DepartmentHeadAdmin(ImportExportModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(ImportExportModelAdmin):
    pass


@admin.register(Curriculum)
class CurriculumAdmin(ImportExportModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    pass
