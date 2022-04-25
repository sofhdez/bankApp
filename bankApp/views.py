from django.http import HttpResponseRedirect
from unicodedata import decimal
from django.shortcuts import render
from .forms import Pago  # form que creamos
from .models import cliente

# Create your views here.



def procesador_pagos(request):
    # form = Pago()
    # context = {
    #     'form': form,
    # }
    
    if request.method == 'POST':
        # Creación del formulario
        form = Pago(request.POST)
        
        # Validar el formulario
        if form.is_valid():
            envia_nombre = form.cleaned_data['envia']  # nombre de quien envía
            recibe_nombre = form.cleaned_data['recibe']  # nombre de quien recibe
            monto_data = decimal.Decimal(form.cleaned_data['monto'])  # monto en decimales
            
            envia_persona = cliente.get(nombre=envia_nombre)
            envia_persona.saldo -= monto_data  # se le RESTA el monto a lo que tiene
            envia_persona.save()
            
            recibe_persona = cliente.get(nombre=recibe_nombre)
            recibe_persona.saldo += monto_data  # se le SUMA el monto a lo que tiene
            recibe_persona.save()
            
            return HttpResponseRedirect('/')
    else:
        form = Pago()
    
    
    context = {
        'form': form,
    }
    
    return render(request, 'index.html', context)
