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
        


        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"}
            )
        
        return data

    def create(self, validated_data):
        validated_data.pop('password2')

        if ((validated_data['student_id'] / 10000) % 100) < 25:
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


class login_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = ['student_id', 'password']

    def validate(self, data):
        try:
            student = Student.objects.get(student_id=data['student_id'])
        except Student.DoesNotExist:
            raise serializers.ValidationError(
                {"Student ID": "Student does not exist"}
            )
        
        if not student.check_password(data['password']):
            raise serializers.ValidationError(
                {"Password": "Wrong Password"}
            )
        
        return data


class logout_serializer(serializers.ModelSerializer):
    pass
