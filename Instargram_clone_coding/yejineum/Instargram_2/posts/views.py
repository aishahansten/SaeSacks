from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

def create(request):
    print('설마?')
    if request.method == 'POST':
        form = PostForm(request.POST)
        print('if문에 들어갓는가')
        if form.is_valid():
            post = form.save()
            print('저장이 되었는가')
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form' : form,
    }
    return render(request, 'posts/create.html', context)