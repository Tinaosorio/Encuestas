from django.shortcuts import render

# Create your views here.
from aplicacion.models import Pregunta


def vista_preguntas(request):
    preguntas = Pregunta.objects.filter(activa=True)
    context = {'preguntas': preguntas}
    return render(request, 'preguntas/preguntas.html', context)
    

def login (request):
    return render(request, "login.html", {} )