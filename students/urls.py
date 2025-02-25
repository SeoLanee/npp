from django.urls import path
from .views import *

urlpatterns = [
    path("", user_view.as_view()),
    path("my-profile", my_profile_view.as_view()),
    path("<int:student_id>", user_detail_view.as_view()),
]