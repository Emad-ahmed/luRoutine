from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from routineMaker.settings import env, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('core.urls')),
    path('', include('faculty.urls')),
    path('', include('routine.urls')),
    path('', include('student.urls')),
    path('', include('semester.urls')),
]

if env.str('ENV_TYPE') == 'DEVELOPMENT':
    import debug_toolbar

    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

