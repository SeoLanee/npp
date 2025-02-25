from django.urls import path
from .views import *

urlpatterns=[
    path('signup', signup_view.as_view()),
    path('login', login_view.as_view()),
    path('logout', logout_view.as_view()),
]