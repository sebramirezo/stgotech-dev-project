from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comat/', views.comat, name='comat'),
    path('buscar/', views.buscar_productos, name='buscar_stdf'),
    path('dashboard/', views.dashboard, name='dashboard'),
]