
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    # path('report_builder/', include('report_builder.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.AUDIO_URL,
                          document_root=settings.AUDIO_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)