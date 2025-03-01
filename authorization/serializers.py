import re
from students.models import Student

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['student_id'] = user.student_id
        token['senior'] = user.senior
        token['major'] = user.major
        return token


class signup_serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['student_id', 'password', 'password2', 'name', 'gender', 'major', 'email']

    def validate(self, data):
        id = data['student_id']
        if not id.isdigit() or len(id) != 8:
            raise serializers.ValidationError(
                {"student_id": "Invalid Student ID format"}
            )
    
        id_int = int(id)
        if not (20000000 <= id_int <= 20300000):
            raise serializers.ValidationError(
                {"student_id": "Invalid Student ID range"}
            )
        
        if not (re.search('[a-zA-z]', data['password']) and re.search('[0-9]', data['password']) and 8 <= len(data['password']) <= 20):
            raise serializers.ValidationError(
                {"password": "Invalid password format"}
            )

        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"}
            )
        
        return data

    def create(self, validated_data):
        validated_data.pop('password2')

        student_id = int(validated_data['student_id'])
        senior = ((student_id // 10000) % 100) != 25
    
        student = Student.objects.create_user(
            student_id=validated_data['student_id'],
            password=validated_data['password'],
            name=validated_data['name'],
            gender=validated_data['gender'],
            major=validated_data['major'],
            email=validated_data['email'],
            senior=senior
        )
        return student


class signup_response_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'email', 'name', 'gender', 'major', 'senior']