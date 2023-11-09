from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

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
    if request.user.is_authenticated:
        return redirect('posts:index')
    else:
        if request.method=="POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                # 회원가입시 자동 로그인
                user = form.save()
                auth_login(request, user)
                return redirect('posts:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    

def delete(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            request.user.delete()
            auth_logout(request)
            return redirect('posts:index')
        else:
            return render(request, 'accounts/delete.html')
    return redirect('posts:index')


def update(request):
    if request.method=="POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/password.html', context)


    