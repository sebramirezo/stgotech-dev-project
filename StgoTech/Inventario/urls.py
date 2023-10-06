from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comat/', views.comat, name='comat'),
    path('incoming/', views.incoming, name='incoming'),
    path('consumos/', views.consumos, name='consumos'),
    path('buscar/', views.buscar_productos, name='buscar_stdf'),
    path('buscar_incoming/', views.buscar_productos_incoming, name='buscar_productos_incoming'),
    path('buscar_consumos/', views.buscar_productos_consumos, name='buscar_productos_consumos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('obtener_datos_comat/', views.obtener_datos_comat, name='obtener_datos_comat'),
]