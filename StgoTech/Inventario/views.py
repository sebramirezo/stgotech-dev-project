from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .forms import *

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

def buscar_productos(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query = request.GET.get('q', '')

    query_awb = request.GET.get('w', '')

    # Realiza la búsqueda de productos por id_stdf
    resultados = Comat.objects.filter(id_stdf__icontains=query)
    resultados_awb = Comat.objects.filter(awb__icontains=query_awb)

    return render(request, 'resultado_busqueda_stdf.html', {'resultados': resultados, 'resultados_awb': resultados_awb, 'query': query, 'query_awb': query_awb})

#VISTA DASHBOARD
def dashboard(request):

    context = {

    }

    return render(request, 'dashboard.html', context)