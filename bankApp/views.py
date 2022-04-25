from django.http import HttpResponseRedirect
from unicodedata import decimal
from django.shortcuts import render
from .forms import Pago  # form que creamos
from .models import cliente
import decimal

# para utilizar el decorador de ATOMIC
from django.db import transaction

# Create your views here.


@transaction.atomic
# para poder hacer ATOMIC las transacciones
# SE EJECUTAN TODAS O NINGUNA
# Hace como un borrador de todas las querys en .save() y
# si una no funciona de manera correcta NO se hace ninguna
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
            # nombre de quien recibe
            recibe_nombre = form.cleaned_data['recibe']
            monto_data = decimal.Decimal(
                form.cleaned_data['monto'])  # monto en decimales

            # envia_persona = cliente.objects.get(nombre=envia_nombre)
            envia_persona = cliente.objects.select_for_update().get(
                                    nombre=envia_nombre)  # para Isolated
            envia_persona.saldo -= monto_data  # se le RESTA el monto a lo que tiene
            envia_persona.save()

            # recibe_persona = cliente.objects.get(nombre=recibe_nombre)
            recibe_persona = cliente.objects.select_for_update().get(
                                    nombre=recibe_nombre)  # para Isolated
            recibe_persona.saldo += monto_data  # se le SUMA el monto a lo que tiene
            recibe_persona.save()

            return HttpResponseRedirect('bankApp')
    else:
        form = Pago()

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)
