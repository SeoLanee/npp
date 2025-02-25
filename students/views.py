from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponseForbidden
from .models import Student
from .serializers import *

class user_view(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        user = request.user
        seniors = Student.objects.filter(
            major=user.major, 
            senior=True, 
            is_active=True
        )
        serializer = get_user_list_serializer(seniors, many=True)
        return Response(serializer.data)
        

class user_detail_view(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, student_id: int):
        if request.user.senior == True :
            return HttpResponseForbidden
        
        student = get_object_or_404(
            Student, 
            id=student_id, 
            is_active=True, 
            senior=True
        )

        serializer = get_user_detail_serializer(student)
        return Response(serializer.data)


class my_profile_view(APIView):
    authentication_classes = [TokenAuthentication]
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