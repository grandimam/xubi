from django.urls import path
from .views import overview, settings

urlpatterns = [
    path('overview/', overview, name='overview'),
    path('settings/', settings, name='settings'),
]
