from django.urls import path

from . import views

urlpatterns = [
    path('', views.procesador_pagos, name='transferencias'),
]
