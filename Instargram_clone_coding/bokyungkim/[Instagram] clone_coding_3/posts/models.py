from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField() # Post 모델의 content field 정의
    image = models.ImageField(blank=True)
    # pillow library 필요