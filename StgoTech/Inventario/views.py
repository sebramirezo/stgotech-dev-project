from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .forms import *
from django.db.models import Q


# Create your views here.

def index(request):
    return redirect('dashboard')

#VISTA COMAT
def comat(request):
    get_form_comat = Comat.objects.all()

    form_comat = ComatForm()

    if request.method == 'POST':
        form_comat = ComatForm(request.POST)
        if form_comat.is_valid():
            form_comat.save()
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
    # get_form_incoming = Incoming.objects.all()

    form_incoming = IncomingForm()

    if request.method == 'POST':
        form_incoming = IncomingForm(request.POST)
        if form_incoming.is_valid():
            form_incoming.save()
            return redirect('/incoming')
    
    else:
        form_comat = ComatForm()

    context = {
        'form_incoming':form_incoming,
    }
    return render(request, 'incoming.html', context)

#VISTA Consumo
def consumos(request):
    # get_form_consumos = Consumo.objects.all()

    form_consumos = ConsumosForm()

    if request.method == 'POST':
        form_consumos = ConsumosForm(request.POST)
        if form_consumos.is_valid():
            form_consumos.save()
            return redirect('/consumos')
    
    else:
        form_consumos = ConsumosForm()

    context = {
        'form_consumos':form_consumos,
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
    query_inco = request.GET.get('r', '')

    resultados_inco = Incoming.objects.filter(
        Q(part_number__icontains = query_inco) 

    )

    # Realiza la búsqueda de productos por id_stdf
    #resultados_part = Incoming.objects.filter(part_number__icontains=query_part)
    # resultados_inc = Incoming.objects.filter(id_stdf=query_inc)

    return render(request, 'resultado_busqueda_incoming.html', { 'resultados_inco': resultados_inco, 'query_inc': query_inco})

def buscar_productos_consumos(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query_sn = request.GET.get('t', '')

    query_bn = request.GET.get('y', '')

    # Realiza la búsqueda de productos por id_stdf
    resultados_sn = Consumos.objects.filter(incoming_id=query_sn)
    # resultados_inc = Incoming.objects.filter(id_stdf=query_inc)

    return render(request, 'resultado_busqueda_consumos.html', { 'resultados_sn': resultados_sn, 'query_bn': query_bn, 'query_sn': query_sn})

#VISTA DASHBOARD
def dashboard(request):

    context = {

    }

    return render(request, 'dashboard.html', context)