from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .models import Post
from .forms import PostForm


# Create your views here.

def portada(request):
    return render(request, 'plantillas/portada.html', {})


def heroes(request):
    return render(request, 'plantillas/heroes.html', {})


def login(request):
    return render(request, 'registration/login.html', {})


def formulario(request):
    return render(request, 'plantillas/questions.html', {})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'plantillas/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'plantillas/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
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
    return render(request, 'plantillas/post_edit.html', {'form': form})

def logout_request(request):
    logout(request)    
    return render(request, 'plantillas/portada.html', {})
 
