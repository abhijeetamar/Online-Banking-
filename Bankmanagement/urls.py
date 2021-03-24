from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('profile/', include("Profile.urls")),
    path('admins/', include("admins.urls")),
    path('email/',include('mail.urls')),
    path('', views.index, name ="home"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
