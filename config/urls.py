from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('', include('login.urls')),
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls)
]
