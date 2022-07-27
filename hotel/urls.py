
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
