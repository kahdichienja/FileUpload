from .views import Home
from .import views
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)