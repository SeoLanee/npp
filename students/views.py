from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from .models import Student
from .serializers import *

class user_view(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200:get_user_list_serializer}
    )
    def get(self, request):
        decoded = JWTAuthentication().authenticate(request);
        _, token = decoded

        if token['senior']:
            return Response({"error": "senior is not available"}, status=403)

        seniors = Student.objects.filter(display=True, major=token['major'], senior=True)
        serializer = get_user_list_serializer(seniors, many=True)

        return Response(data=serializer.data, status=200)


class user_detail_view(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    name='student_id',  
                    in_=openapi.IN_PATH,  
                    type=openapi.TYPE_INTEGER  
                )
            ],
        responses={200:get_user_detail_serializer}
    )
    def get(self, request: HttpRequest, student_id: int):
        decoded = JWTAuthentication().authenticate(request);
        _, token = decoded

        if token['senior']:
            return Response({"error": "senior is not available"}, status=403)

        senior = get_object_or_404(Student, student_id=student_id)
        if token['major'] != senior.major:
            return Response({"error": "senior in other major"}, status=403)      
        
        serializer = get_user_detail_serializer(senior)

        return Response(serializer.data)


class my_profile_view(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: get_user_serializer}
    )
    def get(self, request: HttpRequest):
        decoded = JWTAuthentication().authenticate(request);
        student_id, _ = decoded

        student = get_object_or_404(Student, student_id=student_id)
        serializer= get_user_serializer(data=student)

        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        request_body=update_user_serializer,
        responses={200: update_user_response_serializer}
    )
    def put(self, request: HttpRequest):
        decoded = JWTAuthentication().authenticate(request);
        student_id, _ = decoded

        serializer = update_user_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            student = serializer.update(validated_data=serializer.validated_data, student_id=student_id)
            return Response(student, status=200)

        return Response({"error": serializer.errors}, status=400)

    @swagger_auto_schema(
        responses={200: "string"}
    )
    def delete(self, request: HttpRequest):
        decoded = JWTAuthentication().authenticate(request);
        student_id, _ = decoded

        student = get_object_or_404(Student, student_id=student_id)
        
        student.delete()

        return Response({"message": "The student removed successfully"}, status=200)