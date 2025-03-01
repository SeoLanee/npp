from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import *

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