from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def login(request):
    if request.method=="POST":
        # 로그인 인증에 사용할 데이터 입력받는 폼
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('posts:index')
    

def signup(request):
    if request.mehtod=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)