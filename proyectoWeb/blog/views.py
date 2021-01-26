from django.shortcuts import render

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

