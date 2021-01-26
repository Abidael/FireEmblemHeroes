from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.

def portada(request):
    return render(request, 'plantillas/portada.html', {})


def heroes(request):
    return render(request, 'plantillas/heroes.html', {})


def login(request):
    return render(request, 'plantillas/login.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'plantillas/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'plantillas/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'plantilla/post_edit.html', {'form': form})

def formulario(request):
    return render(request, 'plantillas/questions.html', {})


def publicaciones(request):
    return render(request, 'plantillas/post_list.html', {})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'plantillas/post_list.html', {'posts': posts})
