from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post = form.save()
            return render(request,'posts/index.html')
    else:
        form = PostForm()
    context={
        'form':form
    }
    return render(request,'posts/create.html',context)

@require_POST
def delete(request,pk):
    article = get_object_or_404(Post,pk=pk)
    article.delete()
    return redirect("posts:index")

@require_safe
def read(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        'post':post,
    }
    return render(request,'posts/detail.html',context)