from django.urls import path
from .views import dashboard, connector

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('connector/', connector, name='connector'),
]
