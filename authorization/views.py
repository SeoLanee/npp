from django.shortcuts import render
from django.http import HttpRequest

from rest_framework.views import APIView

class signup_view(APIView):
    def post(self, request: HttpRequest):
        pass


class login_view(APIView):
    def post(self, request: HttpRequest):
        pass


class logout_view(APIView):
    def post(self, request: HttpRequest):
        pass