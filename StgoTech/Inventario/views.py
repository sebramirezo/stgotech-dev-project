from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .forms import *

# Create your views here.

def index(request):
    return redirect('dashboard')

#VISTA COMAT
def comat(request):
    # get_form_comat = Comat.objects.all()

    form_comat = ComatForm()

    if request.method == 'POST':
        form_comat = ComatForm(request.POST)
        if form_comat.is_valid():
            form_comat.save()
            return redirect('/comat')
    
    else:
        form_comat = ComatForm()

    context = {
        'form_comat':form_comat
    }
    return render(request, 'comat.html', context)

def buscar_productos(request):
    # Obtiene el término de búsqueda del usuario desde la URL
    query = request.GET.get('q', '')

    # Realiza la búsqueda de productos por id_stdf
    resultados = Comat.objects.filter(id_stdf=query)

    return render(request, 'comat.html', {'resultados': resultados, 'query': query})

#VISTA DASHBOARD
def dashboard(request):

    context = {

    }

    return render(request, 'dashboard.html', context)