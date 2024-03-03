from django.urls import path

from xubi.app.views import ConnectorCreateView
from xubi.app.views import ConnectorDeleteView
from xubi.app.views import ConnectorPageFormSuccessView
from xubi.app.views import ConnectorUpdateView


urlpatterns = [
    path('', ConnectorCreateView.as_view(), name='connector_page'),
    path('connector/update/<int:pk>', ConnectorUpdateView.as_view(), name='update_connector'),
    path('connector/delete/<int:pk>', ConnectorDeleteView.as_view(), name='delete_connector'),
    path('success/', ConnectorPageFormSuccessView.as_view(), name='connector_page_success'),
]
