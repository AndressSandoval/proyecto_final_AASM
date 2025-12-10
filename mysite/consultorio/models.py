from django.db import models

class PacientePsicologia(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    profesion = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    motivo_consulta_inicial = models.TextField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Psicologo(models.Model):
    id_psicologo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    licencia_colegiado = models.CharField(max_length=50)
    enfoque_terapeutico = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Sesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(PacientePsicologia, on_delete=models.CASCADE)
    id_psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    fecha_sesion = models.DateTimeField()
    hora_sesion = models.TimeField()
    tipo_sesion = models.CharField(max_length=50)
    duracion_minutos = models.IntegerField()
    notas_sesion = models.TextField()
    diagnostico_actual = models.TextField()
    costo_sesion = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Sesión de {self.id_paciente} con {self.id_psicologo} el {self.fecha_sesion}'

class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    nombre_diagnostico = models.CharField(max_length=255)
    descripcion_corta = models.TextField()
    cie_10_codigo = models.CharField(max_length=20)
    dsm_5_codigo = models.CharField(max_length=20)
    tratamientos_sugeridos = models.TextField()
    es_cronico = models.BooleanField()

    def __str__(self):
        return self.nombre_diagnostico

class FacturaPsicologia(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(PacientePsicologia, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    id_sesion_asociada = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    descuento_aplicado = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Factura {self.id_factura} para {self.id_paciente}'

class HistorialClinicoPsicologia(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(PacientePsicologia, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField()
    antecedentes_familiares = models.TextField()
    antecedentes_personales = models.TextField()
    medicamentos_actuales = models.TextField()
    resumen_evolucion = models.TextField()
    id_psicologo_tratante = models.ForeignKey(Psicologo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Historial de {self.id_paciente}'

class RecursoPsicologico(models.Model):
    id_recurso = models.AutoField(primary_key=True)
    nombre_recurso = models.CharField(max_length=255)
    tipo_recurso = models.CharField(max_length=50)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    url_recurso = models.CharField(max_length=255)
    tema_principal = models.CharField(max_length=100)
    publico_objetivo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_recurso
