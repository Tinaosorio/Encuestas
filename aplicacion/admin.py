from django.contrib import admin
from django.utils.html import format_html

from aplicacion.models import Pregunta, Opcion


class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 1


def activar_pregunta(modeladmin, request, preguntas):
    for pregunta in preguntas:
        if pregunta.activa:
            pregunta.activa = False
            pregunta.save()
        else:
            pregunta.activa = True
            pregunta.save()


activar_pregunta.short_description = "Activar / Desactivar Pregunta"


class PreguntaAdminView(admin.ModelAdmin):
    
    inlines = (OpcionInline,)
    list_display = ('id', 'texto', 'opciones', 'activa', 'ver_resultados')
    fieldsets = (
        ("Datos de la pregunta", {'fields': ('texto',)}),
    )
    ordering = ('id',)
    actions = [activar_pregunta,]

    def ver_resultados(self, pregunta):
        return format_html(
            "<a href='/admin/Aplicacion/pregunta/grafica/?id_pregunta={0}' target='_self'> <input type='button' id='{0}' value='{1}' class='default resultados' style='height:22px;width: 90px;padding:1px 1px;'></a>",
            pregunta.id, 'Resultados')

    ver_resultados.short_description = 'Ver Resultados'

    def opciones(self, pregunta):
        lista_opciones = pregunta.opcion_set.all()
        cadena = ""

        for opcion in lista_opciones:
            cadena = cadena + "<li><b>{0})</b> {1}".format(opcion.numeral,
                                                           opcion.texto) + "</li>"

        cadena = "<ul>" + cadena + "</ul>"
        return format_html(cadena)

    opciones.short_description = 'Opciones'


admin.site.register(Pregunta, PreguntaAdminView)
