from django.urls import path
from . import views

app_name = 'consultorio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Paciente URLs
    path('pacientes/', views.PacientePsicologiaListView.as_view(), name='paciente_list'),
    path('pacientes/<int:pk>/', views.PacientePsicologiaDetailView.as_view(), name='paciente_detail'),
    path('pacientes/crear/', views.PacientePsicologiaCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/editar/', views.PacientePsicologiaUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', views.PacientePsicologiaDeleteView.as_view(), name='paciente_delete'),

    # Psicologo URLs
    path('psicologos/', views.PsicologoListView.as_view(), name='psicologo_list'),
    path('psicologos/<int:pk>/', views.PsicologoDetailView.as_view(), name='psicologo_detail'),
    path('psicologos/crear/', views.PsicologoCreateView.as_view(), name='psicologo_create'),
    path('psicologos/<int:pk>/editar/', views.PsicologoUpdateView.as_view(), name='psicologo_update'),
    path('psicologos/<int:pk>/eliminar/', views.PsicologoDeleteView.as_view(), name='psicologo_delete'),

    # Sesion URLs
    path('sesiones/', views.SesionListView.as_view(), name='sesion_list'),
    path('sesiones/<int:pk>/', views.SesionDetailView.as_view(), name='sesion_detail'),
    path('sesiones/crear/', views.SesionCreateView.as_view(), name='sesion_create'),
    path('sesiones/<int:pk>/editar/', views.SesionUpdateView.as_view(), name='sesion_update'),
    path('sesiones/<int:pk>/eliminar/', views.SesionDeleteView.as_view(), name='sesion_delete'),

    # Diagnostico URLs
    path('diagnosticos/', views.DiagnosticoListView.as_view(), name='diagnostico_list'),
    path('diagnosticos/<int:pk>/', views.DiagnosticoDetailView.as_view(), name='diagnostico_detail'),
    path('diagnosticos/crear/', views.DiagnosticoCreateView.as_view(), name='diagnostico_create'),
    path('diagnosticos/<int:pk>/editar/', views.DiagnosticoUpdateView.as_view(), name='diagnostico_update'),
    path('diagnosticos/<int:pk>/eliminar/', views.DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),

    # FacturaPsicologia URLs
    path('facturas/', views.FacturaPsicologiaListView.as_view(), name='facturapsicologia_list'),
    path('facturas/<int:pk>/', views.FacturaPsicologiaDetailView.as_view(), name='facturapsicologia_detail'),
    path('facturas/crear/', views.FacturaPsicologiaCreateView.as_view(), name='facturapsicologia_create'),
    path('facturas/<int:pk>/editar/', views.FacturaPsicologiaUpdateView.as_view(), name='facturapsicologia_update'),
    path('facturas/<int:pk>/eliminar/', views.FacturaPsicologiaDeleteView.as_view(), name='facturapsicologia_delete'),

    # HistorialClinicoPsicologia URLs
    path('historiales/', views.HistorialClinicoPsicologiaListView.as_view(), name='historialclinicopsicologia_list'),
    path('historiales/<int:pk>/', views.HistorialClinicoPsicologiaDetailView.as_view(), name='historialclinicopsicologia_detail'),
    path('historiales/crear/', views.HistorialClinicoPsicologiaCreateView.as_view(), name='historialclinicopsicologia_create'),
    path('historiales/<int:pk>/editar/', views.HistorialClinicoPsicologiaUpdateView.as_view(), name='historialclinicopsicologia_update'),
    path('historiales/<int:pk>/eliminar/', views.HistorialClinicoPsicologiaDeleteView.as_view(), name='historialclinicopsicologia_delete'),

    # RecursoPsicologico URLs
    path('recursos/', views.RecursoPsicologicoListView.as_view(), name='recursopsicologico_list'),
    path('recursos/<int:pk>/', views.RecursoPsicologicoDetailView.as_view(), name='recursopsicologico_detail'),
    path('recursos/crear/', views.RecursoPsicologicoCreateView.as_view(), name='recursopsicologico_create'),
    path('recursos/<int:pk>/editar/', views.RecursoPsicologicoUpdateView.as_view(), name='recursopsicologico_update'),
    path('recursos/<int:pk>/eliminar/', views.RecursoPsicologicoDeleteView.as_view(), name='recursopsicologico_delete'),
]
