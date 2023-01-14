from django.urls import include, path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('pdf_view', views.render_pdf_view_teacher, name='pdf_view'),
]
