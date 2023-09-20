from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    
    #django admin
    path('admin/', admin.site.urls),
    #user management
    path('accounts/', include('django.contrib.auth.urls')),
    #local app
    path('', include('pages.urls')),
    path("accounts/", include("accounts.urls")),
]
