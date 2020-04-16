from django.contrib import admin
from django.urls import path, include
from django.conf import settings


from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entries.urls')),
    path('users/', include('users.urls')),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)