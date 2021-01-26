from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.portada),
    path('post_list/', views.post_list),
    path('portada/', views.post_list),
    path('heroes/', views.heroes),
    path('login/', views.login),
    path('questions/', views.formulario),
]
