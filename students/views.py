from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponseForbidden
from .models import Student
from .serializers import *

class user_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = JWTAuthentication().authenticate(request);
        _, token = response

        if token['senior']:
            return Response({"error": "senior is not available"}, status=403)

        seniors = Student.objects.filter(display=True, major=token['major'], senior=True)
        serializer = get_user_list_serializer(seniors, many=True)

        return Response(data=serializer.data, status=200)


class user_detail_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, student_id: int):
        response = JWTAuthentication().authenticate(request);
        _, token = response

        if token['senior']:
            return Response({"error": "senior is not available"}, status=403)

        senior = get_object_or_404(Student, student_id=student_id)
        if token['major'] != senior.major:
            return Response({"error": "senior in other major"}, status=403)      
        
        serializer = get_user_detail_serializer(senior)

        return Response(serializer.data)


class my_profile_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        serializer = get_user_detail_serializer(request.user)
        return Response(serializer.data)

    def put(self, request: HttpRequest):
        serializer = get_user_detail_serializer(request.data)
        return Response(serializer.data)

    def delete(self, request: HttpRequest):
        student = get_object_or_404(Student, id=request)
        serializer = get_user_detail_serializer(student)
        return Response(serializer.data)