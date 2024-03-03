from django.urls import path

from login.views import LoginPageView


urlpatterns = [
    path('', LoginPageView.as_view(), name='login_page')
]
