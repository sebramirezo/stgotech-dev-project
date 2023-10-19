from django.urls import path
from . import views
from . import exportar_excel

urlpatterns = [
    path('', views.redirect_login, name='redirect_login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('index/', views.index, name='index'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('comat/', views.comat, name='comat'),
    path('incoming/', views.incoming, name='incoming'),
    path('consumos/', views.consumos, name='consumos'),
    path('buscar_productos_inicio/', views.buscar_productos_inicio, name='buscar_productos_inicio'),
    path('buscar/', views.buscar_productos, name='buscar_stdf'),
    path('buscar_incoming/', views.buscar_productos_incoming, name='buscar_productos_incoming'),
    path('buscar_consumos/', views.buscar_productos_consumos, name='buscar_productos_consumos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),
    path('get_pks_by_priority/<str:priority>/', views.get_pks_by_priority, name='get_pks_by_priority'),
    path('obtener_datos_comat/', views.obtener_datos_comat, name='obtener_datos_comat'),
    path('obtener_datos_consumos/', views.obtener_datos_consumos, name='obtener_datos_consumos'),
    path('obtener_datos_incoming/', views.obtener_datos_incoming, name='obtener_datos_incoming'),
    path('buscar_datos_inicio/', views.buscar_datos_inicio, name='buscar_datos_inicio'),
    path('detalle_comat/<int:stdf_pk>/', views.detalle_comat, name='detalle_comat'),
    path('detalle_incoming/<str:sn_batch_pk>/', views.detalle_incoming, name='detalle_incoming'),
    path('detalle_consumos/<int:consumo_pk>/', views.detalle_consumos, name='detalle_consumos'),
    path('detalle_inicio/<int:stdf_pk>/', views.detalle_inicio, name='detalle_inicio'),
    path('exportar_excel_incoming/', exportar_excel.exportar_excel_incoming, name='exportar_excel_incoming'),
]