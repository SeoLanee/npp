import re

from rest_framework import serializers
from students.models import Student


class signup_serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        field = ['student_id', 'password', 'name', 'gender', 'major', 'email']

    def validate(self, data):
        id = data['student_id']
        if len(str(id)) != 8 and not (20000000 <= id <= 20300000):
            raise serializers.ValidationError(
                {"Student ID": "Invalid Student ID"}
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

        if ((validated_data['student_id'] / 10000) % 100) != 25:
            senior=True
        else:
            senior=False

        student = Student.objects.create(
            student_id=validated_data['student_id'],
            password=validated_data['password'],
            name=validated_data['name'],
            gender=validated_data['gender'],
            major=validated_data['major'],
            email=validated_data['email'],
            senior=senior
        )
        return student

