from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from aplicacion.analisis import obtener_analisis, obtener_resultado
from aplicacion.forms import EstudianteForm
from aplicacion.models import Pregunta, Estudiante, PreguntaEstudiante


def vista_preguntas(request):
    if 'usuario_id' in request.session:
        if request.method == 'POST':
            usuario_id = request.session['usuario_id']
            usuario = Estudiante.objects.filter(id=usuario_id)[0]
            for key, value in request.POST.items():
                if key.isdigit():
                    pregunta = Pregunta.objects.filter(id=key)[0]
                    PreguntaEstudiante.create(usuario, pregunta, value)

            return HttpResponseRedirect("/resultados")

        else:
            preguntas = Pregunta.objects.filter(activa=True)
            context = {'preguntas': preguntas}
            return render(request, 'preguntas/preguntas.html', context)
    else:
        return HttpResponseRedirect("/registro")


def get_resultados(request):

    if 'usuario_id' in request.session:
        if request.method == "GET":
            usuario_id = request.session['usuario_id']
            respuestas = PreguntaEstudiante.objects.filter(estudiante__id=usuario_id)

            ar, tipo_ar = obtener_analisis("activo-reflexivo", respuestas)
            mensaje_ar = obtener_resultado("activo-reflexivo", ar, tipo_ar)
            si, tipo_si = obtener_analisis("sensorial-intuitivo", respuestas)
            mensaje_si = obtener_resultado("sensorial-intuitivo", si, tipo_si)
            vv, tipo_vv = obtener_analisis("visual-verbal", respuestas)
            mensaje_vv = obtener_resultado("visual-verbal", vv, tipo_vv)
            sg, tipo_sg = obtener_analisis("secuencial-global", respuestas)
            mensaje_sg = obtener_resultado("secuencial-global", sg, tipo_sg)

            context = {
                       "ar": ar, "tipo_ar": tipo_ar, "mensaje_ar": mensaje_ar,
                       "si": si, "tipo_si": tipo_si, "mensaje_si": mensaje_si,
                       "vv": vv, "tipo_vv": tipo_vv, "mensaje_vv": mensaje_vv,
                       "sg": sg, "tipo_sg": tipo_sg, "mensaje_sg": mensaje_sg,
                       }
            request.session.flush()
            return render(request, "preguntas/resultados.html", context)
        else:
            return HttpResponseRedirect("/registro")
    else:
        return HttpResponseRedirect("/registro")


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

