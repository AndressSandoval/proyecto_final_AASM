from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    PacientePsicologia,
    Psicologo,
    Sesion,
    Diagnostico,
    FacturaPsicologia,
    HistorialClinicoPsicologia,
    RecursoPsicologico
)
from .forms import (
    PacientePsicologiaForm,
    PsicologoForm,
    SesionForm,
    DiagnosticoForm,
    FacturaPsicologiaForm,
    HistorialClinicoPsicologiaForm,
    RecursoPsicologicoForm
)

class IndexView(ListView):
    model = PacientePsicologia
    template_name = "consultorio/index.html"
    context_object_name = "paciente_list"

# PacientePsicologia Views
class PacientePsicologiaListView(ListView):
    model = PacientePsicologia
    template_name = "consultorio/pacientepsicologia_list.html"
    context_object_name = "paciente_list"

class PacientePsicologiaDetailView(DetailView):
    model = PacientePsicologia
    template_name = "consultorio/pacientepsicologia_detail.html"

class PacientePsicologiaCreateView(CreateView):
    model = PacientePsicologia
    form_class = PacientePsicologiaForm
    template_name = "consultorio/pacientepsicologia_form.html"
    success_url = reverse_lazy("consultorio:paciente_list")

class PacientePsicologiaUpdateView(UpdateView):
    model = PacientePsicologia
    form_class = PacientePsicologiaForm
    template_name = "consultorio/pacientepsicologia_form.html"
    success_url = reverse_lazy("consultorio:paciente_list")

class PacientePsicologiaDeleteView(DeleteView):
    model = PacientePsicologia
    template_name = "consultorio/pacientepsicologia_confirm_delete.html"
    success_url = reverse_lazy("consultorio:paciente_list")

# Psicologo Views
class PsicologoListView(ListView):
    model = Psicologo
    template_name = "consultorio/psicologo_list.html"
    context_object_name = "psicologo_list"

class PsicologoDetailView(DetailView):
    model = Psicologo
    template_name = "consultorio/psicologo_detail.html"

class PsicologoCreateView(CreateView):
    model = Psicologo
    form_class = PsicologoForm
    template_name = "consultorio/psicologo_form.html"
    success_url = reverse_lazy("consultorio:psicologo_list")

class PsicologoUpdateView(UpdateView):
    model = Psicologo
    form_class = PsicologoForm
    template_name = "consultorio/psicologo_form.html"
    success_url = reverse_lazy("consultorio:psicologo_list")

class PsicologoDeleteView(DeleteView):
    model = Psicologo
    template_name = "consultorio/psicologo_confirm_delete.html"
    success_url = reverse_lazy("consultorio:psicologo_list")

# Sesion Views
class SesionListView(ListView):
    model = Sesion
    template_name = "consultorio/sesion_list.html"
    context_object_name = "sesion_list"

class SesionDetailView(DetailView):
    model = Sesion
    template_name = "consultorio/sesion_detail.html"

class SesionCreateView(CreateView):
    model = Sesion
    form_class = SesionForm
    template_name = "consultorio/sesion_form.html"
    success_url = reverse_lazy("consultorio:sesion_list")

class SesionUpdateView(UpdateView):
    model = Sesion
    form_class = SesionForm
    template_name = "consultorio/sesion_form.html"
    success_url = reverse_lazy("consultorio:sesion_list")

class SesionDeleteView(DeleteView):
    model = Sesion
    template_name = "consultorio/sesion_confirm_delete.html"
    success_url = reverse_lazy("consultorio:sesion_list")

# Diagnostico Views
class DiagnosticoListView(ListView):
    model = Diagnostico
    template_name = "consultorio/diagnostico_list.html"
    context_object_name = "diagnostico_list"

class DiagnosticoDetailView(DetailView):
    model = Diagnostico
    template_name = "consultorio/diagnostico_detail.html"

class DiagnosticoCreateView(CreateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = "consultorio/diagnostico_form.html"
    success_url = reverse_lazy("consultorio:diagnostico_list")

class DiagnosticoUpdateView(UpdateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = "consultorio/diagnostico_form.html"
    success_url = reverse_lazy("consultorio:diagnostico_list")

class DiagnosticoDeleteView(DeleteView):
    model = Diagnostico
    template_name = "consultorio/diagnostico_confirm_delete.html"
    success_url = reverse_lazy("consultorio:diagnostico_list")

# FacturaPsicologia Views
class FacturaPsicologiaListView(ListView):
    model = FacturaPsicologia
    template_name = "consultorio/facturapsicologia_list.html"
    context_object_name = "facturapsicologia_list"

class FacturaPsicologiaDetailView(DetailView):
    model = FacturaPsicologia
    template_name = "consultorio/facturapsicologia_detail.html"

class FacturaPsicologiaCreateView(CreateView):
    model = FacturaPsicologia
    form_class = FacturaPsicologiaForm
    template_name = "consultorio/facturapsicologia_form.html"
    success_url = reverse_lazy("consultorio:facturapsicologia_list")

class FacturaPsicologiaUpdateView(UpdateView):
    model = FacturaPsicologia
    form_class = FacturaPsicologiaForm
    template_name = "consultorio/facturapsicologia_form.html"
    success_url = reverse_lazy("consultorio:facturapsicologia_list")

class FacturaPsicologiaDeleteView(DeleteView):
    model = FacturaPsicologia
    template_name = "consultorio/facturapsicologia_confirm_delete.html"
    success_url = reverse_lazy("consultorio:facturapsicologia_list")

# HistorialClinicoPsicologia Views
class HistorialClinicoPsicologiaListView(ListView):
    model = HistorialClinicoPsicologia
    template_name = "consultorio/historialclinicopsicologia_list.html"
    context_object_name = "historialclinicopsicologia_list"

class HistorialClinicoPsicologiaDetailView(DetailView):
    model = HistorialClinicoPsicologia
    template_name = "consultorio/historialclinicopsicologia_detail.html"

class HistorialClinicoPsicologiaCreateView(CreateView):
    model = HistorialClinicoPsicologia
    form_class = HistorialClinicoPsicologiaForm
    template_name = "consultorio/historialclinicopsicologia_form.html"
    success_url = reverse_lazy("consultorio:historialclinicopsicologia_list")

class HistorialClinicoPsicologiaUpdateView(UpdateView):
    model = HistorialClinicoPsicologia
    form_class = HistorialClinicoPsicologiaForm
    template_name = "consultorio/historialclinicopsicologia_form.html"
    success_url = reverse_lazy("consultorio:historialclinicopsicologia_list")

class HistorialClinicoPsicologiaDeleteView(DeleteView):
    model = HistorialClinicoPsicologia
    template_name = "consultorio/historialclinicopsicologia_confirm_delete.html"
    success_url = reverse_lazy("consultorio:historialclinicopsicologia_list")

# RecursoPsicologico Views
class RecursoPsicologicoListView(ListView):
    model = RecursoPsicologico
    template_name = "consultorio/recursopsicologico_list.html"
    context_object_name = "recursopsicologico_list"

class RecursoPsicologicoDetailView(DetailView):
    model = RecursoPsicologico
    template_name = "consultorio/recursopsicologico_detail.html"

class RecursoPsicologicoCreateView(CreateView):
    model = RecursoPsicologico
    form_class = RecursoPsicologicoForm
    template_name = "consultorio/recursopsicologico_form.html"
    success_url = reverse_lazy("consultorio:recursopsicologico_list")

class RecursoPsicologicoUpdateView(UpdateView):
    model = RecursoPsicologico
    form_class = RecursoPsicologicoForm
    template_name = "consultorio/recursopsicologico_form.html"
    success_url = reverse_lazy("consultorio:recursopsicologico_list")

class RecursoPsicologicoDeleteView(DeleteView):
    model = RecursoPsicologico
    template_name = "consultorio/recursopsicologico_confirm_delete.html"
    success_url = reverse_lazy("consultorio:recursopsicologico_list")
