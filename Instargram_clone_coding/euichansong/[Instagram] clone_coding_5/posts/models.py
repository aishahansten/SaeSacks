from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    # blank=True 옵션으로 빈 문자열도 저장될수 있게 조건 설정
    image = models.ImageField(blank=True)