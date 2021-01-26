from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
#Funcion portada, recibe un requerimiento que levanta una plantilla y renderizando.
def portada(request):
    return render(request, 'plantillas/portada.html', {})

def questions(request):
    return render(request, 'plantillas/questions.html', {})

def heroes(request):
    return render(request, 'plantillas/heroes.html', {})

def login(request):
    return render(request, 'plantillas/login.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'plantillas/post_list.html', {'posts': posts})


