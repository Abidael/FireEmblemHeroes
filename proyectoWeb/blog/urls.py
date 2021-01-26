from django.urls import path
from . import views

# Este patrón mostrará a Django que views.Portada es el lugar correcto al que ir si alguien ingresa a tu sitio web con la dirección 'http://127.0.0.1:8000/'.


urlpatterns = [
    # localhost:8000/
    path('', views.portada, name='portada'),

    # localhost:8000/Questions
    path('questions/', views.questions, name='questions'),

    # localhost:8000/Heroes
    path('heroes/', views.heroes, name='heroes'),
    
]