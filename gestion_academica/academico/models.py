from django.db import models

# Relación Muchos a Uno: Profesor y Curso 
# Un Profesor puede impartir varios Cursos.
# Un Curso pertenece a un solo Profesor.

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE) # Borrado en cascada
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
# Relación Muchos a Muchos: Estudiante y Curso
# Un Estudiante puede estar inscrito en varios Cursos.
# Un Curso puede estar inscrito por varios Estudiantes.

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

# Entidad Intermedia para la relación Muchos a Muchos
class Inscripcion(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Finalizado', 'Finalizado'),
    ]
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')
    nota_final = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.id_estudiante} - {self.id_curso}"

# Relación Uno a Uno: Estudiante y Perfil
# Un Estudiante tiene un solo Perfil.
# Un Perfil pertenece a un solo Estudiante.

class Perfil(models.Model):
    id_estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE) # implementación con OneToOneField
    biografia = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    redes = models.URLField(blank=True)

    def __str__(self):
        return f"Perfil de {self.id_estudiante}"

