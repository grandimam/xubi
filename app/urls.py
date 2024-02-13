from django.urls import path
from .views import overview, create_connector, delete_connector

urlpatterns = [
    path('overview/', overview, name='overview'),
    path('connectors/', create_connector, name='connectors')
]
