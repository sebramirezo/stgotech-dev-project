from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .forms import *
from django.db.models import Q , Sum
from django.http.response import JsonResponse
import json
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, permission_required

# Vistas relacionadas al inicio y cierre de sesión
def redirect_login(request):
    return redirect('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def cerrar_sesion(request):
    logout(request)
    return redirect('/login')

####################################################


#VISTAS DE INICIO
#REDIRIGE A LA PAGINA PRINCIPAL INICIO
def index(request):
    return redirect('dashboard')






#OBTIENE LOS DATOS QUE RELACIONADOS A LA BUSQUEDA QUE SE REALIZO
# def buscar_datos_inicio(request):
#     draw = int(request.GET.get('draw', 0))
#     start = int(request.GET.get('start', 0))
#     length = int(request.GET.get('length', 10))
#     search_value = request.GET.get('n', '')

#     resultados = []

#     # Consulta en Comat y realiza JOIN con Incoming y Consumos
#     resultados += list(
#         Incoming.objects.filter(
#             Q(part_number__icontains=search_value) | Q(stdf_fk__stdf_pk__icontains=search_value)
#         ).select_related('stdf_fk', 'ubicacion_fk', 'categoria_fk', 'owner_fk').values(
#             "sn_batch_pk",
#             "categoria_fk__name_categoria",
#             "part_number",
#             "categoria_fk__name_categoria",
#             "descripcion",
#             "stdf_fk__stdf_pk",
#             "qty",
#             "saldo",
#             "stdf_fk__awb",
#             "stdf_fk__num_manifiesto",
#             "owner_fk__name_owner",
#             "ubicacion_fk__name_ubicacion",
#             "f_vencimiento"
#         ).annotate(
#             qty_extraida_total=Sum('consumos__qty_extraida')  # Suma de la cantidad extraída
#         ).distinct()  # Utiliza distinct para obtener un registro por número de parte
#         [start:start + length]
#     )

#     records_filtered = len(resultados)

#     return JsonResponse({
#         "data": resultados,
#         "draw": draw,
#         "recordsTotal": records_filtered,  # Total de registros sin filtrar
#         "recordsFiltered": records_filtered  # Total de registros después del filtrado
#     })



#BUSCADOR DE LA PAGINA DE INICIO, REDIRIGE AL RESULTADO DE BUSQUEDA DE LA PAGINA DE INICIO
def buscar_productos_inicio(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query_inicio = request.GET.get('n', '')

    return render(request, 'resultado_busqueda_inicio.html', {'query_inicio':query_inicio})

def buscar_datos_inicio(request):
    draw = int(request.GET.get('draw', 0))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('n', '')

    # Consulta en Incoming
    query_incoming = Incoming.objects.filter(
        Q(part_number__icontains=search_value) | Q(stdf_fk__stdf_pk__icontains=search_value)
    ).select_related('stdf_fk', 'ubicacion_fk', 'categoria_fk', 'owner_fk')

    total_records_incoming = query_incoming.count()

    resultados_incoming = list(
        query_incoming.values(
            "sn_batch_pk",
            "categoria_fk__name_categoria",
            "part_number",
            "descripcion",
            "stdf_fk__stdf_pk",
            "qty",
            "saldo",
            "stdf_fk__awb",
            "stdf_fk__num_manifiesto",
            "owner_fk__name_owner",
            "ubicacion_fk__name_ubicacion",
            "f_vencimiento"
        ).annotate(
            qty_extraida_total=Sum('consumos__qty_extraida')
        ).distinct()
    )[start:start + length]  # Ajustar la paginación aquí

    # Consulta para obtener Comats sin Incoming relacionado
    query_comats_sin_incoming = Comat.objects.filter(incoming__isnull=True)
    total_records_comats_sin_incoming = query_comats_sin_incoming.count()
    resultados_comats_sin_incoming = list(
        query_comats_sin_incoming.values("stdf_pk", "awb", "hawb", "prioridad")
    )[start:start + length]  # Ajustar la paginación aquí

    # Crear el diccionario principal "data"
    data = {
        "draw": draw,
        "recordsTotal": total_records_incoming,
        "recordsFiltered": total_records_incoming,
        "data_incoming": resultados_incoming,
        "data_comats_sin_incoming": resultados_comats_sin_incoming,   
    }

    return JsonResponse(data)






#OBTIENE LOS DATOS PARA REALIZAR EL DETALLE DE LA PAGINA DE INICIO
def detalle_inicio(request, sn_batch_pk):

    detalle_inicio = Incoming.objects.get(sn_batch_pk=sn_batch_pk)   

    comat_data = detalle_inicio.stdf_fk

    consumos_data = detalle_inicio.consumos_set.all()

    return render(request,'detalle_inicio.html' , {'detalle_inicio':detalle_inicio, 'comat_data' : comat_data, 'consumos_data':consumos_data })


@login_required 
def comat(request):
    get_form_comat = Comat.objects.all()
    total_cif = 0
    if request.method == 'POST':
        form_comat = ComatForm(request.POST)
        if form_comat.is_valid():
            # Obtén el objeto Comat sin guardarlo aún
            comat = form_comat.save(commit=False)
            
            comat.usuario = request.user

            # Realiza la suma de fob, flete y seguro
            total_cif= comat.fob + comat.flete + comat.seguro
            
            # Guarda el objeto Comat con la cif actualizada
            comat.sum_cif = total_cif
            comat.save()
            
            return redirect('/comat')
    else:
        form_comat = ComatForm()

    context = {
        'form_comat':form_comat,
        'get_form_comat':get_form_comat,
    }
    return render(request, 'comat.html', context)


#BUSCADOR DE COMAT
def buscar_productos(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query_comat = request.GET.get('c', '')

    return render(request, 'resultado_busqueda_stdf.html', {'query_comat':query_comat})
    #resultados = Comat.objects.filter(id_stdf__icontains=query)
    #resultados_awb = Comat.objects.filter(awb__icontains=query_awb)

    
    #'resultados_awb': resultados_awb, 'query': query, 'query_awb': query_awb



# def obtener_datos_comat(request):
#     # Obtén los parámetros enviados por DataTables
#     draw = int(request.GET.get('draw', 0))
#     start = int(request.GET.get('start', 0))
#     length = int(request.GET.get('length', 10))  # Número de registros por página

#     # Realiza la consulta teniendo en cuenta la paginación
#     comat_data = Comat.objects.all()[start:start + length]

#     # Formatea los datos en un formato compatible con DataTables
#     data = []
#     for comat in comat_data:
#         data.append({
#             "stdf_pk": comat.stdf_pk,
#             "awb": comat.awb,
#         })

#     return JsonResponse({
#         "data": data,
#         "draw": draw,
#         "recordsTotal": Comat.objects.count(),  # Total de registros sin filtrar
#         "recordsFiltered": Comat.objects.count(),  # Total de registros después del filtrado (puedes ajustar esto según tus necesidades)
#     })



#OBTIENE LOS RESULTADOS CON MÁS RELACION QUE TIENE LA BUSQUEDA
def obtener_datos_comat(request):
    # Obtén los parámetros enviados por DataTables
    draw = int(request.GET.get('draw', 0))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))  # Número de registros por página
    search_value = request.GET.get('c', '')  # Término de búsqueda

    comat_data = Comat.objects.all()
    
    if search_value:
        comat_data = comat_data.filter(Q(stdf_pk__icontains=search_value) | Q(awb__icontains=search_value)| Q(hawb__icontains=search_value))
        


    # Realizar la consulta teniendo en cuenta la paginación
    comat_data = comat_data[start:start + length]


    # Formatea los datos en un formato compatible con DataTables
    data = []
    for comat in comat_data:
        data.append({
            "stdf_pk": comat.stdf_pk,
            "awb": comat.awb,
            "hawb":comat.hawb,
            "num_manifiesto":comat.num_manifiesto,
            "sum_cif":comat.sum_cif,
            "bodega_fk":comat.bodega_fk.name_bodega,
            
        })
    
    if search_value:
        records_filtered = Comat.objects.filter(stdf_pk__icontains=search_value).count()
    else:
    # Si no hay término de búsqueda, simplemente cuenta todos los registros
        records_filtered = Comat.objects.count()

    return JsonResponse({
        "data": data,
        "draw": draw,
        "recordsTotal": Comat.objects.count(),  # Total de registros sin filtrar
        "recordsFiltered": records_filtered  # Total de registros después del filtrado (puedes ajustar esto según tus necesidades)
    })

#OBTIENE LOS DATOS PARA REALIZAR EL DETALLE POR LA ID
def detalle_comat(request, stdf_pk):
    detalle_comat = Comat.objects.get(stdf_pk=stdf_pk)    
    return render(request,'detalle_comat.html' , {'detalle_comat':detalle_comat})






#VISTA DE INCOMING QUE VALIDA EL FORMULARIO Y LO GUARDA Y REDIRIGE A LA PAGINA DE INCOMING
@login_required 
def incoming(request):
    get_form_incoming = Incoming.objects.all()
    total_unit_cost = 0

    if request.method == 'POST':
        form_incoming = IncomingForm(request.POST)
        if form_incoming.is_valid():
            # Guarda el formulario de Incoming
            incoming = form_incoming.save(commit=False)

            incoming.usuario = request.user

            total_unit_cost =  incoming.qty * incoming.u_purchase_cost 
            # Copia el valor de cantidad_extraida a la columna saldo

            incoming.total_u_purchase_cost = total_unit_cost
            incoming.saldo = incoming.qty
            incoming.save()

            return redirect('/incoming')
    
    else:
        form_incoming = IncomingForm()

    context = {
        'form_incoming': form_incoming,
        'get_form_incoming': get_form_incoming, 
    }
    return render(request, 'incoming.html', context)


#GUARDA EL VALOR QUE SE BUSCO Y REDIRIGE A LA PAGINA DE RESULTADOS
def buscar_productos_incoming(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query_inco = request.GET.get('e', '')
    
    return render(request, 'resultado_busqueda_incoming.html', {'query_inco':query_inco})
    
    # Realiza la búsqueda de productos por id_stdf
    #resultados_part = Incoming.objects.filter(part_number__icontains=query_part)
    # resultados_inc = Incoming.objects.filter(id_stdf=query_inc)


#OBTIENE LOS DATOS RELACIONADOS A LA BUSQUEDA 
def obtener_datos_incoming(request):
    # Obtén los parámetros enviados por DataTables
    draw = int(request.GET.get('draw', 0))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))  # Número de registros por página
    search_value = request.GET.get('e', '')  # Término de búsqueda

    incoming_data = Incoming.objects.all()
    
    if search_value:
        incoming_data = incoming_data.filter(Q(part_number__icontains = search_value) | Q(sn_batch_pk__icontains=search_value))
        


    # Realizar la consulta teniendo en cuenta la paginación
    incoming_data = incoming_data[start:start + length]


    # Formatea los datos en un formato compatible con DataTables
    data = []
    for incoming in incoming_data:
        data.append({
            "sn_batch_pk":incoming.sn_batch_pk,
            "categoria_fk":incoming.categoria_fk.name_categoria,
            "part_number":incoming.part_number,
            "descripcion": incoming.descripcion,
            "qty":incoming.qty,
            "f_vencimiento":incoming.f_vencimiento,
            "saldo":incoming.saldo,
        })
    
    if search_value:
        records_filtered = Incoming.objects.filter(part_number__icontains=search_value).count()
    else:
    # Si no hay término de búsqueda, simplemente cuenta todos los registros
        records_filtered = Incoming.objects.count()

    return JsonResponse({
        "data": data,
        "draw": draw,
        "recordsTotal": Incoming.objects.count(),  # Total de registros sin filtrar
        "recordsFiltered": records_filtered  # Total de registros después del filtrado (puedes ajustar esto según tus necesidades)
    })


def detalle_incoming(request, sn_batch_pk):
    detalle_incoming = Incoming.objects.get(sn_batch_pk=sn_batch_pk)    
    return render(request,'detalle_incoming.html' , {'detalle_incoming':detalle_incoming})



#VISTAS DE CONSUMO

#VISTA DE CONSUMO QUE VALIDA EL FORMULARIO Y LO GUARDA Y REDIRIGE A LA VISTA DE CONSUMOS
@login_required 
def consumos(request):
    form_consumos = ConsumosForm()
    if request.method == 'POST':
        form_consumos = ConsumosForm(request.POST)
        if form_consumos.is_valid():
            consumo = form_consumos.save()  # Guardar el formulario de Consumos

            consumo.usuario = request.user
            # Obtener el registro correspondiente en Incoming
            incoming = consumo.incoming_fk

            incoming.saldo -=consumo.qty_extraida
            

            # Actualizar el valor de saldo en el registro de Incoming
            incoming.save()

            return redirect('/consumos')

    context = {
        'form_consumos': form_consumos,
    }
    return render(request, 'consumos.html', context)




   
#GUARDA LA BUSQUEDA QUE SE REALIZO Y REDIRIGE A LA PAGINA DE RESULTADOS DE CONSUMOS
def buscar_productos_consumos(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query_consu = request.GET.get('t', '')

    return render(request, 'resultado_busqueda_consumos.html', {'query_consu': query_consu})



#OBTIENE LOS DATOS RELACIONADOS A LA BUSQUEDA DE CONSUMOS
def obtener_datos_consumos(request):
    # Obtén los parámetros enviados por DataTables
    draw = int(request.GET.get('draw', 0))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))  # Número de registros por página
    search_value = request.GET.get('t', '')  # Término de búsqueda

    # Inicializa la consulta sin filtrar
    consumos_data = Consumos.objects.all()

    # Realiza la consulta teniendo en cuenta el término de búsqueda en incoming_fk
    if search_value:
            consumos_data = consumos_data.filter(Q(incoming_fk=search_value))

    # Realiza la paginación
    consumos_data = consumos_data[start:start + length]

    # Formatea los datos en un formato compatible con DataTables
    data = []
    for consumo in consumos_data:
        data.append({
            "consumo_pk": consumo.consumo_pk,
            "incoming_fk": consumo.incoming_fk.sn_batch_pk,
            "f_transaccion": consumo.f_transaccion,
            "matricula_aeronave": consumo.matricula_aeronave,
            "orden_consumo": consumo.orden_consumo,
            "qty_extraida": consumo.qty_extraida,
        })

    if search_value:
        records_filtered = Consumos.objects.filter(incoming_fk=search_value).count()
    else:
    # Si no hay término de búsqueda, simplemente cuenta todos los registros
        records_filtered = Consumos.objects.count()

    return JsonResponse({
        "data": data,
        "draw": draw,
        "recordsTotal": Consumos.objects.count(),  # Total de registros sin filtrar
        "recordsFiltered": records_filtered,
        
    })

#OBTIENE LOS DATOS PARA REALIZAR EL DETALLE DE CONSUMOS
def detalle_consumos(request, consumo_pk):
    detalle_consumos = Consumos.objects.get(consumo_pk=consumo_pk)   

    incoming_data = detalle_consumos.incoming_fk

    return render(request,'detalle_consumos.html' , {'detalle_consumos':detalle_consumos, 'incoming_data' : incoming_data })






def detalle_inicio(request, stdf_pk):
    draw = int(request.GET.get('draw', 0))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))  # Número de registros por página

    comat_data = Comat.objects.get(stdf_pk=stdf_pk)

    # Tabla de Incoming
    incoming_objects = Incoming.objects.filter(stdf_fk=comat_data)
    incoming_objects_paginated = incoming_objects[start:start + length]

    incoming_data_list = []

    for incoming_obj in incoming_objects_paginated:
        incoming_data_list.append({
            "sn_batch_pk": incoming_obj.sn_batch_pk,
            "part_number": incoming_obj.part_number,
            "f_incoming": incoming_obj.f_incoming,
            "descripcion": incoming_obj.descripcion,
            "po":incoming_obj.po,
            "qty":incoming_obj.qty,
            "u_purchase_cost":incoming_obj.u_purchase_cost,
            "total_u_purchase_cost":incoming_obj.total_u_purchase_cost,
            "f_vencimiento":incoming_obj.f_vencimiento,
            "saldo":incoming_obj.saldo,
            "observaciones":incoming_obj.observaciones,
            "categoria_fk":incoming_obj.categoria_fk.name_categoria,
            "clasificacion_fk":incoming_obj.clasificacion_fk.name_clasificacion,
            "ubicacion_fk":incoming_obj.ubicacion_fk.name_ubicacion,
            "uom_fk":incoming_obj.uom_fk.name_uom,
            "owner_fk":incoming_obj.owner_fk.name_owner,
            "condicion_fk":incoming_obj.condicion_fk.name_condicion,
            "ficha_fk":incoming_obj.ficha_fk.name_ficha,
    })

    incoming_records_total = incoming_objects.count()
    incoming_records_filtered = incoming_records_total  # Opcionalmente, puedes aplicar filtros aquí

    # Tabla de Consumos
    consumos_objects = Consumos.objects.filter(incoming_fk__in=incoming_objects)
    consumos_objects_paginated = consumos_objects[start:start + length]

    consumos_data_list = []

    for consumos_obj in consumos_objects_paginated:
        consumos_data_list.append({
                "incoming_fk":consumos_obj.incoming_fk.sn_batch_pk,
                "orden_consumo":consumos_obj.orden_consumo,
                "f_transaccion":consumos_obj.f_transaccion,
                "qty_extraida":consumos_obj.qty_extraida,
                "matricula_aeronave":consumos_obj.matricula_aeronave,
                "observaciones":consumos_obj.observaciones,
        })

    consumos_records_total = consumos_objects.count()
    consumos_records_filtered = consumos_records_total  # Opcionalmente, puedes aplicar filtros aquí

    data = {
        "draw": draw,
        "recordsTotal": incoming_records_total,
        "recordsFiltered": incoming_records_filtered,
        "comat_data": {
                "stdf_pk": comat_data.stdf_pk,
                "awb": comat_data.awb,
                "hawb": comat_data.hawb,
                "num_manifiesto": comat_data.num_manifiesto,
                "sum_cif": comat_data.sum_cif,
                "corr_interno" : comat_data.corr_interno,
                "psc": comat_data.pcs,
                "peso": comat_data.peso,
                "f_control": comat_data.f_control,
                "f_manifiesto": comat_data.f_manifiesto,
                "f_recepcion": comat_data.f_recepcion,
                "f_stdf": comat_data.f_stdf,
                "fob": comat_data.fob,
                "flete": comat_data.flete,
                "seguro": comat_data.seguro,
                "bodega_fk": comat_data.bodega_fk.name_bodega,
                "origen_fk": comat_data.origen_fk.name_origen,
                "estado_fk": comat_data.estado_fk.estado,
            },
        "incoming_data": incoming_data_list,
        "consumos_data": consumos_data_list,
    }

    if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        return JsonResponse(data)
    else:
        # Si no es una solicitud AJAX, renderiza una plantilla HTML
        return render(request, 'detalle_inicio.html', {
            "comat_data": comat_data,
            "incoming_data_list": incoming_data_list,
            "incoming_recordsTotal": incoming_records_total,
            "incoming_recordsFiltered": incoming_records_filtered,
            "consumos_data": consumos_data_list,
            "consumos_recordsTotal": consumos_records_total,
            "consumos_recordsFiltered": consumos_records_filtered,
        })

















































# ## Test
# def obtener_datos_stdf_incoming(request):

#     term = request.GET.get('q', '')

#     stdf_data = Comat.objects.filter(stdf_pk__icontains=term).values('stdf_pk')[:20]

#     # stdf_data = Comat.objects.all().values('stdf_pk')
#     stdf_list = list(stdf_data)
    
#     # Convierte la lista de diccionarios a una lista de objetos JSON
#     stdf_json = [{'stdf_pk': item['stdf_pk']} for item in stdf_list]
    
#     return JsonResponse({'stdf_data': stdf_json}, safe=False)





#VISTA DASHBOARD
def dashboard(request):
    comat_data = Comat.objects.all().order_by()[:10]
    incoming_data = Incoming.objects.all()
    context = {
        'comat_data':comat_data,
        'incoming_data':incoming_data

    }

    return render(request, 'dashboard.html', context)