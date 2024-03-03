from django.urls import path

from xubi.login.views import LoginPageView


urlpatterns = [
    path('', LoginPageView.as_view(), name='login_page')
]
