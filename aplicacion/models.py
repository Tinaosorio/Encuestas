from django.db import models

class Pregunta(models.Model):
    texto = models.TextField(verbose_name='texto')
    activa = models.BooleanField(verbose_name='activa', default=True)

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class Opcion(models.Model):
    numeral = models.CharField(verbose_name='numeral', max_length=2)
    texto = models.CharField(verbose_name='texto', max_length=300)
    votos = models.IntegerField(verbose_name='votos', default=0)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}) {1} | votos: {2}".format(self.numeral, self.texto, self.votos)

    class Meta:
        verbose_name = 'Opcion'
        verbose_name_plural = 'Opciones'


