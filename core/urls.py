from django.urls import path
from django.conf import settings
from .views import home,login_view,register,logout_view
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'), 
    path('login/',login_view,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout_view,name='logout')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
