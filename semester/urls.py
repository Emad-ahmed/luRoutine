from django.urls import path
from . import views

app_name = 'semester'

urlpatterns = [
    path('semesters/', views.SemesterListView.as_view(), name='semester_list'),
    path('semester/create/', views.SemesterCreateView.as_view(), name='semester_create'),
    path('semester/update/', views.SemesterUpdateView.as_view(), name='semester_update'),
    path('semester/<int:pk>/delete/', views.SemesterDeleteView, name='semester_delete'),


    path('offers/', views.CourseOfferingListView.as_view(), name='offer_list'),
    path('offer/create/', views.CourseOfferingCreateView.as_view(), name='offer_create'),
    path('offer/update/', views.CourseOfferUpdateView.as_view(), name='offer_update'),
    path('offers/<int:pk>/delete/', views.CourseOfferDeleteView, name='offer_delete'),


    path('distributions/', views.CourseDistributionList.as_view(), name='dist_list'),
    path('distribution/create/', views.CourseDistributionCreateView.as_view(), name='dist_create'),
    path('distribution/update/', views.CourseDistributionUpdateView.as_view(), name='dist_update'),
    path('distribution/<int:pk>/delete/', views.CourseDistributionDeleteView, name='dist_delete'),

    path('getBatchWiseCourse/', views.getBatchCourses, name='batch_course'),
    path('getOfferedSections/', views.getOfferedSection, name='offered_section'),
    path('getOfferedParents/', views.getOfferedParent, name='offered_parent'),
]
