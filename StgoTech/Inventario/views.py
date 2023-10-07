from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .forms import *
from django.db.models import Q , F


# Create your views here.

def index(request):
    return redirect('dashboard')

#VISTA COMAT
def comat(request):
    get_form_comat = Comat.objects.all()

    if request.method == 'POST':
        form_comat = ComatForm(request.POST)
        if form_comat.is_valid():
            # Obtén el objeto Comat sin guardarlo aún
            comat = form_comat.save(commit=False)
            
            # Realiza la suma de fob, flete y seguro
            comat.sum_cif = comat.fob + comat.flete + comat.seguro
            
            # Guarda el objeto Comat con la cif actualizada
            comat.save()
            
            return redirect('/comat')
    else:
        form_comat = ComatForm()

    context = {
        'form_comat':form_comat,
        'get_form_comat':get_form_comat,
    }
    return render(request, 'comat.html', context)


#VISTA Incoming
def incoming(request):
    get_form_incoming = Incoming.objects.all()
    total_unit_cost = 0
    if request.method == 'POST':
        form_incoming = IncomingForm(request.POST)
        if form_incoming.is_valid():
            # Guarda el formulario de Incoming
            incoming = form_incoming.save(commit=False)
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

#VISTA Consumo
def consumos(request):
    form_consumos = ConsumosForm()
    saldo_actualizado = 0
    if request.method == 'POST':
        form_consumos = ConsumosForm(request.POST)
        if form_consumos.is_valid():
            consumo = form_consumos.save()  # Guardar el formulario de Consumos

            # Obtener el registro correspondiente en Incoming
            incoming = consumo.incoming_fk

            saldo_actualizado += incoming.qty
            # Calcular el nuevo valor de saldo
            saldo_actualizado -=  consumo.qty_extraida

            # Actualizar el valor de saldo en el registro de Incoming
            incoming.saldo = saldo_actualizado
            incoming.save()

            return redirect('/consumos')

    context = {
        'form_consumos': form_consumos,
    }
    return render(request, 'consumos.html', context)


def buscar_productos(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query = request.GET.get('q', '')

    # Realiza la búsqueda de productos por id_stdf o awb
    resultados = Comat.objects.filter(
        Q(stdf_pk__icontains=query) | Q(awb__icontains=query)| Q(hawb__icontains=query)
    )

    return render(request, 'resultado_busqueda_stdf.html', {'resultados': resultados, 'query':query})
    #resultados = Comat.objects.filter(id_stdf__icontains=query)
    #resultados_awb = Comat.objects.filter(awb__icontains=query_awb)

    
    #'resultados_awb': resultados_awb, 'query': query, 'query_awb': query_awb

def buscar_productos_incoming(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query_inco = request.GET.get('e', '')

    resultados_inco = Incoming.objects.filter(
        Q(part_number__icontains = query_inco) | Q(sn_batch_pk__icontains=query_inco) 
    )

    return render(request, 'resultado_busqueda_incoming.html', {'resultados_inco': resultados_inco, 'query_inco':query_inco})
    
    # Realiza la búsqueda de productos por id_stdf
    #resultados_part = Incoming.objects.filter(part_number__icontains=query_part)
    # resultados_inc = Incoming.objects.filter(id_stdf=query_inc)

   

def buscar_productos_consumos(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query_consu = request.GET.get('t', '')



    # Realiza la búsqueda de productos por id_stdf
    resultados_consu = Consumos.objects.filter(
        Q(incoming_fk = query_consu) 
    )
    # resultados_inc = Incoming.objects.filter(id_stdf=query_inc)

    return render(request, 'resultado_busqueda_consumos.html', { 'resultados_consu': resultados_consu, 'query_consu': query_consu})

#VISTA DASHBOARD
def dashboard(request):
    comat_data = Comat.objects.all().order_by()[:10]
    incoming_data = Incoming.objects.all()
    context = {
        'comat_data':comat_data,
        'incoming_data':incoming_data

    }

    return render(request, 'dashboard.html', context)