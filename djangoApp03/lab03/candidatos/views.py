from django.shortcuts import render
from .models import Candidato


def index(request):
    Lista_de_datos=Candidato.objects.order_by('-id')
    context ={
        'data_list':Lista_de_datos
    }
    return render(request,'candidatos/index.html',context)