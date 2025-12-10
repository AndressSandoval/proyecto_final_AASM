from django import forms
from .models import (
    PacientePsicologia,
    Psicologo,
    Sesion,
    Diagnostico,
    FacturaPsicologia,
    HistorialClinicoPsicologia,
    RecursoPsicologico
)

class PacientePsicologiaForm(forms.ModelForm):
    class Meta:
        model = PacientePsicologia
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

class PsicologoForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = '__all__'
        widgets = {
            'fecha_sesion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'hora_sesion': forms.TimeInput(attrs={'type': 'time'}),
        }

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = '__all__'

class FacturaPsicologiaForm(forms.ModelForm):
    class Meta:
        model = FacturaPsicologia
        fields = '__all__'
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class HistorialClinicoPsicologiaForm(forms.ModelForm):
    class Meta:
        model = HistorialClinicoPsicologia
        fields = '__all__'
        widgets = {
            'fecha_actualizacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class RecursoPsicologicoForm(forms.ModelForm):
    class Meta:
        model = RecursoPsicologico
        fields = '__all__'
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }
