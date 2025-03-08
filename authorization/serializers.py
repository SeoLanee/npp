import re
from .utils import generate_key
from .models import Email, WhitelistEmailValidator
from students.models import Student

from django.shortcuts import get_object_or_404
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


class email_serializer(serializers.ModelSerializer):
    class Meta:
        model=Email
        fields=['email']
        extra_kwargs = {
            'email': {'validators': [WhitelistEmailValidator(allowlist=['sogang.ac.kr'])]}
        }

    def validate(self, data):
        return data

    def create(self, data):
        if Email.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(
                {'email': 'given email already exists'},
                code=400
            )

        return Email.objects.create(
            email=data['email'],
            validated=False,
            key=generate_key()
        )
    
    def update(self, data):
        email = get_object_or_404(Email, email=data['email'])
        email.key = generate_key()
        email.save(update_fields=['key'])
        return email


class email_validation_serializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['email', 'key']
        extra_kwargs = {
            'email': {'validators': []}  # 자동 중복 검사 제거
        }

    def validate(self, data):
        try:
            email = Email.objects.get(email=data['email'])
        except Email.DoesNotExist:
            raise serializers.ValidationError(
                detail={"email": "Given email does not exists"},
                code=400
            )   
        if not email.key == data['key']:
            raise serializers.ValidationError(
                detail={"key": "Given key does not match"},
                code=401
            )
        return data
    
    def update(self, validated_data):
        email = Email.objects.get(email=validated_data['email'])
        email.validated = True
        email.save(update_fields=['validated'])
        return email