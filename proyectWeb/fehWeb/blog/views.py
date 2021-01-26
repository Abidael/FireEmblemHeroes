from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def portada(request):
    return render(request, 'plantillas/portada.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'plantillas/post_list.html', {'posts': posts})



