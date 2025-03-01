from rest_framework import serializers
from .models import Student

class get_user_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender']



class get_user_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender', 'major', 'kakao_id', 'insta_id', 'message', 'senior']



class get_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender', 'major', 'kakao_id', 'insta_id', 'message', 'senior']



class update_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender', 'major', 'kakao_id', 'insta_id', 'message', 'senior']



class delete_user_serializer(serializers.ModelSerializer):
    pass