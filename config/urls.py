from django.contrib import admin
from django.urls import path, include
from config.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls'))
]


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)