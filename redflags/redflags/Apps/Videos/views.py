from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Ubicacion
from .forms import FormularioForm
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import CreateView, ListView

# Create your views here.


def vista_formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('inicio')
       
    else:
      form = FormularioForm()

    return render (request,"formulario.html",{'form':form})

def vista_listado_mapa(request):
    lista=Ubicacion.objects.all()  # asignar valores desde los modelos a la variable lista
    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json

def inicio(request):
    return render (request,'inicio.html')

def vista_mapa(request):
    return render (request,"mapa.html")

class formulario(CreateView):
    model=Ubicacion
    form_class=FormularioForm
    template_name="formulario.html"
    success_url=reverse_lazy("inicio")



