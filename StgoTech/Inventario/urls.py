from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comat/', views.comat, name='comat'),
    path('incoming/', views.incoming, name='incoming'),
    path('buscar/', views.buscar_productos, name='buscar_stdf'),
    path('buscar_incoming/', views.buscar_productos_incoming, name='buscar_productos_incoming'),
    path('dashboard/', views.dashboard, name='dashboard'),
]