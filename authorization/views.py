from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .utils import send_email
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainpairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class signup_view(APIView):
    @swagger_auto_schema(
            request_body=signup_serializer,
            responses={201: signup_response_serializer}
    )
    def post(self, request: HttpRequest):
        serializer = signup_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            student = serializer.save()
            response_data = {
                "student_id": student.student_id,
                "email": student.email,
                "name": student.name,
                "gender": student.gender,
                "major": student.major,
                "senior": student.senior,
            }
            return Response(response_data, status=201)

        return Response(serializer.errors, status=400)


class email_view(APIView):
    @swagger_auto_schema(
            request_body=email_serializer,
            responses={201: 'Created'}
    )
    def post(self, request: HttpRequest):
        serializer = email_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            email = serializer.save()
            send_email(email.email, email.key)
            return Response({'message': 'Created'}, status=201)
        return Response(serializer.errors)
    
    @swagger_auto_schema(
            request_body=email_serializer,
            responses={200: 'Resend succeed'}
    )
    def put(self, request: HttpRequest):
        serializer = email_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            email = serializer.update(serializer.validated_data)
            send_email(email.email, email.key)
            return Response({'message': 'Resend succeed'}, status=200)
        return Response(serializer.errors)


class email_validation_view(APIView):
    @swagger_auto_schema(
            request_body=email_validation_serializer,
            responses={200: 'Validation succeed'}
    )
    def post(self, request: HttpRequest):
        serializer = email_validation_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.update(serializer.validated_data)
            return Response({'message': 'Validation succeed'}, status=200)
        
        return Response(serializer.errors, status=400)