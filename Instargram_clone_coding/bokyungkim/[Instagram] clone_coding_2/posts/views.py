from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)


#CREATE
from .forms import PostForm

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'posts/create.html', context)



def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("posts:index")
