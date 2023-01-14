from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('batches/', views.BatchListView.as_view(), name='batch_list'),
    path('batch/create/', views.BatchCreateView.as_view(), name='batch_create'),

    path('sections/', views.SectionListView.as_view(), name='section_list'),
    path('section/create/', views.SectionCreateView.as_view(), name='section_create'),
]
