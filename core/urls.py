from django.urls import path
from django.conf import settings
from .views import home, about
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'), 
    path('about/',about,name='about')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
