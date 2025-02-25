from django.db import models
from django.contrib.auth.models import User

class Gender(models.IntegerChoices):
    MALE = 0, "Male"
    FEMALE = 1, "Female"

class Major(models.IntegerChoices):
    HUMANITIES = 0, "인문대학"
    KOREAN_LITERATURE = 1, "국어국문학과"
    HISTORY = 2, "사학과"
    PHILOSOPHY = 3, "철학과"
    RELIGIOUS_STUDIES = 4, "종교학과"
    ENGLISH_LITERATURE = 5, "영문학과"
    AMERICAN_STUDIES = 6, "미국문화학과"
    EUROPEAN_STUDIES = 7, "유럽학과"
    GERMAN_STUDIES = 8, "독일학과"
    FRENCH_STUDIES = 9, "프랑스학과"
    ECONOMY = 10, "경제학과"
    BUSINESS = 11, "경영학과"
    MEDIA_ART_SCIENCE = 12, "미디어아트학과"
    JOURNALISM = 13, "신문방송학과"
    MEDIA_ENTERTAINMENT = 14, "미디어엔터테인먼트학과"
    ART_TECHNOLOGY = 15, "아트테크놀로지학과"
    GLOBAL_KOREAN_STUDIES = 16, "글로벌한국학과"
    MATHEMATICS = 17, "수학과"
    PHYSICS = 18, "물리학과"
    CHEMISTRY = 19, "화학과"
    BIOLOGY = 20, "생명과학과"
    ELECTRICAL_ENGINEERING = 21, "전자공학과"
    COMPUTER_ENGINEERING = 22, "컴퓨터공학과"
    CHEMICAL_ENGINEERING = 23, "화공생명공학과"
    MECHANICAL_ENGINEERING = 24, "기계공학과"
    ARTIFICIAL_INTELLIGENCE = 25, "인공지능학과"
    SYSTEM_SEMICONDUCTOR_ENGINEERING = 26, "시스템반도체공학과"
    FREE_MAJOR = 27, "AI자유전공학부"


class StudentBase(models.Model):
    student_id = models.CharField(max_length=8, unique=True, primary_key=True);
    name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=Gender.choices)
    major = models.IntegerField(choices=Major.choices);
    email = models.EmailField(unique=True)
    kakao_id = models.CharField(max_length=32, unique=True, blank=True, null=True)
    insta_id = models.CharField(max_length=32, unique=True, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    senior = models.BooleanField(null=True)
    is_active = models.BooleanField(default=False)