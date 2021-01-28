from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.portada),
    path('post_list/', views.post_list, name='post_list'),
    path('portada/', views.portada, name='portada'),
    path('heroes/', views.heroes),
    path('login/', views.login),
    path('questions/', views.formulario),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'), 
    path("logout/", views.logout_request, name="logout"),   
]
