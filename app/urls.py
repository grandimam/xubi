from django.urls import path
from .views import overview, create_connector, get_cloud_cost_data

urlpatterns = [
    path('overview/', overview, name='overview'),
    path('overview/cloud-cost-data/', get_cloud_cost_data, name='get_cloud_cost_data'),
    path('connectors/', create_connector, name='connectors')
]
