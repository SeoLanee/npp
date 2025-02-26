from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.decorators import api_view

class signup_view(APIView):
    @api_view(['POST'])
    def post(self, request: HttpRequest):
        pass


class login_view(APIView):
    @api_view(['POST'])
    def post(self, request: HttpRequest):
        pass


class logout_view(APIView):
    @api_view(['POST'])
    def post(self, request: HttpRequest):
        pass