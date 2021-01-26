from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.portada),
    path('post_list/', views.post_list),
]
