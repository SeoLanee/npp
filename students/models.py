from django.db import models
from django.contrib.auth.models import User

class major:
    Humanities          = 0
    KoreanLiterature    = 1
    History             = 2
    Philosophy          = 3
    ReligiousStudies    = 4
    EnglishLiterature   = 5
    AmericanStudies     = 6
    EuropeanStudies     = 7
    GermanStudies       = 8
    FrenchStudies       = 9
    Economy             = 10
    Business            = 11
    MediaArtScience     = 12
    Journalism          = 13    
    MediaEntertainment  = 14
    ArtTechnology       = 15
    GlobalKoreanStudies = 16
    Mathematics         = 17
    Physics             = 18
    Chemistry           = 19
    LifeSciences        = 20
    ElectricalEngineering   = 21
    ComputerEngineering     = 22
    ChemicalEngineering     = 23
    MechanicalEngineering   = 24
    ArtificialIntelligence  = 25
    SystemSemiconductorEngineering = 26
    FreeMajor          = 27
    CHOICES = (
        (0, "인문대학"),
        (1, "국어국문학과"),
        (2, "사학과"),
        (3, "철학과"),
        (4, "종교학과"),
        (5, "영문학과"),
        (6, "미국문화학과"),
        (7, "유럽학과"),
        (8, "독일학과"),
        (9, "프랑스학과"),
        (10, "경제학과"),
        (11, "경영학과"),
        (12, "미디어아트학과"),
        (13, "신문방송학과"),
        (14, "미디어엔터테인먼트학과"),
        (15, "아트테크놀로지학과"),
        (16, "글로벌한국학과"),
        (17, "수학과"),
        (18, "물리학과"),
        (19, "화학과"),
        (20, "생명과학과"),
        (21, "전자공학과"),
        (22, "컴퓨터공학과"),
        (23, "화공생명공학과"),
        (24, "기계공학과"),
        (25, "인공지능학과"),
        (26, "시스템반도체공학과"),
        (27, "AI자유전공학부"),
    )

class gender:
    male    = 0
    female  = 1
    CHOICES=(
        (0, male),
        (1, female)
    )


class StudentBase(models.Model):
    student_id = models.CharField(max_length=8, unique=True, primary_key=True);
    name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=gender.CHOICES)
    major = models.IntegerField(choices=major.CHOICES);
    email = models.EmailField(unique=True)
    kakao_id = models.CharField(max_length=32, blank=True, null=True)
    insta_id = models.CharField(max_length=32, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    
class Senior(StudentBase):
    display = models.BooleanField(default=False)

class Junior(StudentBase):
    pass
