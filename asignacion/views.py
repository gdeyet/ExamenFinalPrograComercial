from django.shortcuts import render

from django.contrib import messages
from .forms import CursoForm
from asignacion.models import Curso, Estudio


def curso_nuevo(request):

    if request.method == "POST":

        formulario = CursoForm(request.POST)

        if formulario.is_valid():

            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])

            for alumno_id in request.POST.getlist('alumnos'):

                actuacion = Estudio(alumno_id=alumno_id, curso_id = curso.id)

                actuacion.save()

            messages.add_message(request, messages.SUCCESS, 'Curso Guardado Exitosamente')

    else:

        formulario = CursoForm()

    return render(request, 'Curso/Curso_editar.html', {'formulario': formulario})