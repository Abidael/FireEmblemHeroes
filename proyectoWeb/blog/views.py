from django.shortcuts import render

# Create your views here.
#Funcion portada, recibe un requerimiento que levanta una plantilla y renderizando.
def portada(request):
    return render(request, 'blog/portada.html', {})

def questions(request):
    return render(request, 'blog/questions.html', {})

def heroes(request):
    return render(request, 'blog/heroes.html', {})

