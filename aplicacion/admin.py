from django.contrib import admin
from django.utils.html import format_html

from aplicacion.models import Pregunta, Opcion, TipoPregunta

from django.contrib.admin import AdminSite

admin.site.site_url = "/admin/preguntas/"


class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 0


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
    list_display = ('id', 'texto', 'opciones', 'activa')
    fieldsets = (
        ("Datos de la pregunta", {'fields': ('texto', 'tipo')}),
    )
    ordering = ('id',)
    actions = [activar_pregunta,]


    def opciones(self, pregunta):
        lista_opciones = pregunta.opcion_set.all()
        cadena = ""

        for opcion in lista_opciones:
            cadena = cadena + "<li><b>{0})</b> {1}".format(opcion.tipo,
                                                           opcion.texto) + "</li>"

        cadena = "<ul>" + cadena + "</ul>"
        return format_html(cadena)

    opciones.short_description = 'Opciones'


admin.site.register(Pregunta, PreguntaAdminView)
admin.site.register(TipoPregunta)
