from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Gender(models.IntegerChoices):
    MALE = 0, "Male"
    FEMALE = 1, "Female"

class Major(models.IntegerChoices):
    HUMANITIES                          = 0, "인문대학"
    ENGLISH_LITERATURE                  = 1, "영문학과"
    EUROPEAN_STUDIES                    = 2, "유럽학과"
    ECONOMY                             = 3, "경제학과"
    BUSINESS                            = 4, "경영학과"
    MEDIA_ART_SCIENCE                   = 5, "미디어아트학과"
    MATHEMATICS                         = 6, "수학과"
    PHYSICS                             = 7, "물리학과"
    CHEMISTRY                           = 8, "화학과"
    BIOLOGY                             = 9, "생명과학과"
    ELECTRICAL_ENGINEERING              = 10, "전자공학과"
    COMPUTER_ENGINEERING                = 11, "컴퓨터공학과"
    CHEMICAL_ENGINEERING                = 12, "화공생명공학과"
    MECHANICAL_ENGINEERING              = 13, "기계공학과"
    ARTIFICIAL_INTELLIGENCE             = 14, "인공지능학과"
    SYSTEM_SEMICONDUCTOR_ENGINEERING    = 15, "시스템반도체공학과"
    FREE_MAJOR                          = 16, "AI자유전공학부"

class StudentManager(BaseUserManager):
    def create_user(
            self, 
            student_id,
            password,
            name,
            gender,
            major,
            email,
            senior,
            kakao_id=None,
            insta_id=None,
            message=None,
            **extra_fields
        ):
        
        if not password:
            raise ValueError("Password is required")

        student = self.model(
            student_id=student_id,
            name=name,
            gender=gender,
            major=major,
            email=email,
            kakao_id=kakao_id,
            insta_id=insta_id,
            message=message,
            senior=senior,
            **extra_fields
        )
        student.set_password(password)
        student.save(using=self._db)
        return student
    
    def create_superuser(self, name, gender, major, email, senior, password, **extra_fields):
        return self.create_user(
            name=name,
            gender=gender,
            major=major,
            email=email,
            senior=senior,
            password=password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            **extra_fields,
        )



class Student(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=8, unique=True, primary_key=True);
    name = models.CharField(max_length=32)
    gender = models.IntegerField(choices=Gender.choices)
    major = models.IntegerField(choices=Major.choices);
    email = models.EmailField(unique=True)
    kakao_id = models.CharField(max_length=32, unique=True, blank=True, null=True)
    insta_id = models.CharField(max_length=32, unique=True, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    senior = models.BooleanField(null=True)
    
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)

    objects = StudentManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name', 'gender', 'major', 'email', 'senior']