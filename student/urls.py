from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('batches/', views.BatchListView.as_view(), name='batch_list'),
    path('batch/create/', views.BatchCreateView.as_view(), name='batch_create'),
    path('batch/update/', views.BatchUpdateView.as_view(), name='batch_update'),
    path('batch/<int:pk>/delete/', views.BatchDeleteView, name='batch_delete'),

    path('sections/', views.SectionListView.as_view(), name='section_list'),
    path('section/create/', views.SectionCreateView.as_view(), name='section_create'),
    path('section/update/', views.SectionUpdateView.as_view(), name='section_update'),
    path('section/<int:pk>/delete/', views.SectionDeleteView, name='section_delete'),
]
