from django.urls import path, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.SimpleRouter(trailing_slash=False)
urlpatterns = [
    path('register', views.UserCreateAPIView.as_view()),
    path('login', obtain_auth_token),
]
urlpatterns += router.urls
