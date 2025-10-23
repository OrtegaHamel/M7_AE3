
```python
from academico.models import Profesor, Curso, Estudiante, Inscripcion, Perfil

# Crear profesores
profesor1 = Profesor.objects.create(nombre="Juan Pérez", email="juan@example.com")
profesor2 = Profesor.objects.create(nombre="Ana Gómez", email="ana@example.com")

# Crear cursos
curso1 = Curso.objects.create(id_profesor=profesor1, nombre="Matemáticas", descripcion="Curso de matemáticas básicas.")
curso2 = Curso.objects.create(id_profesor=profesor1, nombre="Física", descripcion="Curso de física clásica.")
curso3 = Curso.objects.create(id_profesor=profesor2, nombre="Literatura", descripcion="Curso de literatura moderna.")

# Crear estudiantes
estudiante1 = Estudiante.objects.create(nombre="Carlos Ruiz", email="carlos@example.com")
estudiante2 = Estudiante.objects.create(nombre="María López", email="maria@example.com")

# Inscribir estudiantes en cursos
Inscripcion.objects.create(id_estudiante=estudiante1, id_curso=curso1, estado="Activo")
Inscripcion.objects.create(id_estudiante=estudiante1, id_curso=curso2, estado="Activo", nota_final=8.5)
Inscripcion.objects.create(id_estudiante=estudiante2, id_curso=curso3, estado="Finalizado", nota_final=9.0)

# Crear perfiles
Perfil.objects.create(id_estudiante=estudiante1, biografia="Apasionado por las ciencias.", foto="perfiles/carlos.jpg", redes="https://example.com/carlos")
Perfil.objects.create(id_estudiante=estudiante2, biografia="Amante de la lectura.", redes="https://example.com/maria")

```
