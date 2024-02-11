from django.urls import path
from .views import overview, connectors

urlpatterns = [
    path('overview/', overview, name='overview'),
    path('connectors/', connectors, name='connectors'),
]
