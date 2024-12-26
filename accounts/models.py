from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'
        
    # 기본 필드
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    birth_date = models.DateField()
    
    # 선택 필드
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    # 휴대폰 번호 검증을 위한 RegexValidator
    phone_number_validator = RegexValidator(
        regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$'
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[phone_number_validator],
        unique=True,
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username