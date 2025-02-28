from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('signup', signup_view.as_view()),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh-token', TokenRefreshView.as_view(), name='token_obtain_pair'),
]