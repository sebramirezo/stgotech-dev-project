from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):

    form_comat = ComatForm()

    if request.method == 'POST':
        form_comat = ComatForm(request.POST)

    context = {
        'comats':form_comat
    }
    return render(request, 'base.html', context)
