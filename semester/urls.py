from django.urls import path
from . import views

app_name = 'semester'

urlpatterns = [
    path('semesters/', views.SemesterListView.as_view(), name='semester_list'),
    path('semester/create/', views.SemesterCreateView.as_view(), name='semester_create'),

    path('offers/', views.CourseOfferingListView.as_view(), name='offer_list'),
    path('offer/create/', views.CourseOfferingCreateView.as_view(), name='offer_create'),

    path('distributions/', views.CourseDistributionList.as_view(), name='dist_list'),
    path('distribution/create/', views.CourseDistributionCreateView.as_view(), name='dist_create'),

    path('getBatchWiseCourse/', views.getBatchCourses, name='batch_course'),
    path('getOfferedSections/', views.getOfferedSection, name='offered_section'),
    path('getOfferedParents/', views.getOfferedParent, name='offered_parent'),
]
