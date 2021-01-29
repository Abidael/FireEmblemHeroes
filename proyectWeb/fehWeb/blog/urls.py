from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.portada),
    path('post_list/', views.post_list, name='post_list'),    
    path('heroes/', views.heroes, name='heroes'),
    path('login/', views.login,  ),
    path('questions/', views.formulario, name='questions'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'), 
    path('logout/', views.logout_request, name="logout"), 
    path('', views.login_request, name="login"), 
]
