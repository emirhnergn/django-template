from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('templateapp.urls')),
    path('trigger-error/', trigger_error)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
