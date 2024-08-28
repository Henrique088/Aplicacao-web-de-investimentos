from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.logar, name="logar"),
    path('cadastro/', views.cadastro, name= "cadastro"),
    path('logar/', views.logar, name= "logar"),
    path('redirecionamento/', views.redirecionamento, name= "redirecionamento"),
    
]
