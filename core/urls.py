from django.urls import path
from django.conf import settings
from .views import home,login,register
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'), 
    
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
