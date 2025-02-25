from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

from django.http import HttpRequest

class user_view(APIView):
    def get(self, request: HttpRequest):
        pass


class user_detail_view(APIView):
    def get(self, request: HttpRequest, student_id: int):
        pass


class my_profile_view(APIView):
    def get(self, request: HttpRequest):
        pass

    def put(self, request: HttpRequest):
        pass

    def delete(self, request: HttpRequest):
        pass