from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)


def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'posts/create.html', context)

def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect("posts:index")