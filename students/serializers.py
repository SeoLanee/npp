import re
import bleach

from rest_framework import serializers
from .models import Student

class get_user_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender']


class get_user_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'gender', 'major', 'kakao_id', 'insta_id', 'message', 'senior']


class get_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender', 'major', 'email', 'kakao_id', 'insta_id', 'message', 'senior', 'display'] 


class update_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'kakao_id', 'insta_id', 'message', 'display'] 
        extra_kwargs = {field: {'required': False, 'validators': []} for field in fields}


    def validate(self, data):
        def validate_kakao_id(kakao_id: str) -> bool:
            return bool(re.fullmatch(r'^[a-z0-9_.]{4,15}$', kakao_id))

        def validate_insta_id(insta_id: str) -> bool:
            return bool(re.fullmatch(r'^[a-zA-Z0-9_.]{1,30}$', insta_id))

        def validate_message(message: str) -> str:
            return bleach.clean(message)

        student_id = self.context.get('student_id')
        try:
            student = Student.objects.get(student_id=student_id)
        except:
            raise serializers.ValidationError(
                {"student": "Something wrong with student"}
            )
        
        kakao_id = data.get('kakao_id')
        insta_id = data.get('insta_id')

        if kakao_id and kakao_id != student.kakao_id:
            if Student.objects.filter(kakao_id=kakao_id).exists():
                raise serializers.ValidationError(
                    {"kakao_id": "The kakao ID already exists"}
                )
            if not validate_kakao_id(kakao_id):
                raise serializers.ValidationError(
                    {"kakao_id": "Invalid kakaotalk ID format"}
                )
        
        if insta_id and insta_id != student.insta_id:
            if Student.objects.filter(insta_id=insta_id).exists():
                raise serializers.ValidationError(
                    {"insta_id": "The instagram ID already exists"}
                )
            if not validate_insta_id(insta_id):
                raise serializers.ValidationError(
                    {"insta_id": "Invalid instagram ID format"}
                )
        
        if data.get('message'):
            data['message'] = validate_message(data['message'])

        return data
    
    def update(self, validated_data, student_id):
        try:
            student = Student.objects.get(student_id=student_id)  
        except Student.DoesNotExist:
            raise serializers.ValidationError({"error": "Student not found"})  
            
        for field in ['name', 'kakao_id', 'insta_id', 'message', 'display']:
            if field in validated_data:
                setattr(student, field, validated_data[field])  
                
        student.save()  

        return {
                "student_id": student.student_id,
                "name": student.name,
                "gender": student.gender,
                "major": student.major,
                "email": student.email.email,
                "kakao_id": student.kakao_id,
                "insta_id": student.insta_id,
                "message": student.message,
                "senior": student.senior,
                "display": student.display,
            }
    

class update_user_response_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=["student_id", "name", "gender", "major", "email", "kakao_id", "insta_id", "message", "senior", "display"]
