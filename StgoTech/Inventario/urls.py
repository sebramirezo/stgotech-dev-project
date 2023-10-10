from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comat/', views.comat, name='comat'),
    path('incoming/', views.incoming, name='incoming'),
    path('consumos/', views.consumos, name='consumos'),
    path('buscar_productos_inicio/', views.buscar_productos_inicio, name='buscar_productos_inicio'),
    path('buscar/', views.buscar_productos, name='buscar_stdf'),
    path('buscar_incoming/', views.buscar_productos_incoming, name='buscar_productos_incoming'),
    path('buscar_consumos/', views.buscar_productos_consumos, name='buscar_productos_consumos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('obtener_datos_comat/', views.obtener_datos_comat, name='obtener_datos_comat'),
    path('obtener_datos_consumos/', views.obtener_datos_consumos, name='obtener_datos_consumos'),
    path('obtener_datos_incoming/', views.obtener_datos_incoming, name='obtener_datos_incoming'),
    path('obtener_stdf_incoming/', views.obtener_datos_stdf_incoming, name='obtener_stdf_incoming'),
    path('buscar_datos_inicio/', views.buscar_datos_inicio, name='buscar_datos_inicio'),
    path('detalle_comat/<int:stdf_pk>/', views.detalle_comat, name='detalle_comat'),
    path('detalle_incoming/<str:sn_batch_pk>/', views.detalle_incoming, name='detalle_incoming'),
    path('detalle_consumos/<int:consumo_pk>/', views.detalle_consumos, name='detalle_consumos'),

]