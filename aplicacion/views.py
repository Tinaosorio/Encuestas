from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from aplicacion.forms import EstudianteForm
from aplicacion.models import Pregunta, Estudiante, PreguntaEstudiante


def vista_preguntas(request):
    if request.method == 'POST':
        usuario_id = (request.session['usuario_id'])
        usuario = Estudiante.objects.filter(id=usuario_id)[0]
        for key, value in request.POST.items():
            print(key)
            if key.isdigit():
                print(key)
                pregunta = Pregunta.objects.filter(id=key)[0]
                PreguntaEstudiante.create(usuario, pregunta, value)

        return HttpResponseRedirect("/resultados")

    else:
        preguntas = Pregunta.objects.filter(activa=True)
        context = {'preguntas': preguntas}
        return render(request, 'preguntas/preguntas.html', context)


def get_resultados(request):

    if request.method == "GET":
        return render(request, "preguntas/resultados.html")


def registro_usuario(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            request.session['usuario_id'] = usuario.id
            return HttpResponseRedirect("/preguntas")
    else:
        form = EstudianteForm()

    context = {"form": form}
    return render(request, 'usuarios/registro_usuario.html', context)

