import imp
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy
from .forms import MyPasswordResetForm, MySetPasswordForm

app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name="user_logout"),
    path('account/reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),


    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),


    path('password-reset-confirm/<str:uidb64>/<str:token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),


    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),



]
