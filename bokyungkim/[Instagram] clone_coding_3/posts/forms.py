from django import forms  
from .models import Post 

# Post model에 대한 ModelForm 정의
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Post 모델과 연결, 모든 field 나타나도록 
        fields = '__all__'
