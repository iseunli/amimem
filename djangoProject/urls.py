from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cosplayers.urls')),
    path('', include('django.contrib.auth.urls')),
    path('authorization/', include('django.contrib.auth.urls')),
    path('authorization/', include('authorization.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT,)
