from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *

class signup_view(APIView):
    @api_view(['POST'])
    def post(self, request: HttpRequest):
        serializer = signup_serializer(request.data)
        return Response(serializer.data)