from django.db import models
from django.contrib import admin

# Create your models here.
class Alumno(models.Model):

    nombre  =   models.CharField(max_length=30)

    carne  =   models.CharField(max_length=30)

    fecha_nacimiento = models.DateField()


    def __str__(self):

        return self.nombre


class Curso(models.Model):

    nombre    = models.CharField(max_length=60)

    anio      = models.IntegerField()

    alumnos   = models.ManyToManyField(Alumno, through='Estudio')


    def __str__(self):

        return self.nombre



class Estudio (models.Model):

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class EstudioInLine(admin.TabularInline):

    model = Estudio
    extra = 1


class AlumnoAdmin(admin.ModelAdmin):

    inlines = (EstudioInLine,)


class CursoAdmin (admin.ModelAdmin):

    inlines = (EstudioInLine,)