from django.db import models


class TipoPregunta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Pregunta'
        verbose_name_plural = 'Tipos de Preguntas'


class Pregunta(models.Model):
    texto = models.TextField(verbose_name='texto')
    activa = models.BooleanField(verbose_name='activa', default=True)
    tipo = models.ForeignKey(TipoPregunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class Opcion(models.Model):
    TIPO_I = 1
    TIPO_II = 2
    TIPOS = ((TIPO_I, "Tipo 1"), (TIPO_II, "Tipo 2"))
    tipo = models.IntegerField(verbose_name='tipo', choices=TIPOS, default=TIPO_I)
    texto = models.CharField(verbose_name='texto', max_length=300)
    votos = models.IntegerField(verbose_name='votos', default=0)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}) {1} | votos: {2}".format(self.tipo, self.texto, self.votos)

    class Meta:
        verbose_name = 'Opcion'
        verbose_name_plural = 'Opciones'


class Estudiante(models.Model):
    I_SEMESTRE = "I Semestre"
    II_SEMESTRE = "II Semestre"
    III_SEMESTRE = "III Semestre"
    IV_SEMESTRE = "IV Semestre"
    V_SEMESTRE = "V Semestre"

    SI = "Si"
    NO = "No"

    RESPUESTAS = ((SI, "Si"), (NO, "No"))

    SEMESTRES = ((I_SEMESTRE, "I Semestre"), (II_SEMESTRE, "II Semestre"),
                 (III_SEMESTRE, "III Semestre"), (IV_SEMESTRE, "IV Semestre"),
                 (V_SEMESTRE, "V Semestre"))

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=15, unique=True)
    semestre = models.CharField(max_length=15, choices=SEMESTRES, default=I_SEMESTRE)
    programacion = models.CharField(max_length=3, choices=RESPUESTAS, default=SI)
    pregunta = models.ManyToManyField(Pregunta, through="PreguntaEstudiante")


class PreguntaEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.IntegerField()

    def __str__(self):
        return self.pregunta.texto + " " + str(self.respuesta)
    @classmethod
    def create(cls, estudiante, pregunta, respuesta):
        pregunta_estudiante = cls(estudiante=estudiante, pregunta=pregunta, respuesta=respuesta)
        pregunta_estudiante.save()
        return pregunta_estudiante
