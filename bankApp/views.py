from django.shortcuts import render

# Create your views here.

from .forms import Pago  # form que creamos


def procesador_pagos(request):
    form = Pago()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
