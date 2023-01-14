from django.urls import path

from . import views

app_name = 'faculty'

urlpatterns = [
    path('faculties/', views.FacultyListView.as_view(), name='faculty_list'),
    path('faculty/create/', views.FacultyCreateView.as_view(), name='faculty_create'),
    path('faculty/update/', views.FacultyUpdateView.as_view(), name='faculty_update'),

    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('department/create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('department/update/', views.DepartmentUpdateView.as_view(), name='department_update'),

    path('programs/', views.ProgramListView.as_view(), name='program_list'),
    path('program/create/', views.ProgramCreateView.as_view(), name='program_create'),
    path('program/update/', views.ProgramUpdateView.as_view(), name='program_update'),

    path('curriculums/', views.CurriculumListView.as_view(), name='curriculum_list'),
    path('curriculum/create/', views.CurriculumCreateView.as_view(), name='curriculum_create'),

    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher/create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/update/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/reset/', views.teacher_account_reset, name='teacher_account_reset'),

    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
]
