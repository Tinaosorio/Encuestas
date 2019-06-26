from django import forms

from aplicacion.models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre',
            'apellido',
            'semestre',
            'programacion'
        ]
        labels = [
            'Nombre',
            'Apellidos',
            'Semestre',
            'Le gusta la programacion?'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'programacion': forms.Select(attrs={'class': 'form-control'})
        }