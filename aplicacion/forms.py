from django import forms

from aplicacion.models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre',
            'apellido',
            'documento',
            'semestre',
            'programacion'
        ]
        labels = {
            'programacion': '¿Le gusta la programacion?'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]+'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'programacion': forms.Select(attrs={'class': 'form-control'})
        }