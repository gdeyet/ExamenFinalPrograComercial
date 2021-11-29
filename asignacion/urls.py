from django.conf.urls import url
from . import views

urlpatterns = [
    url('asignacion/nueva/', views.curso_nuevo, name='curso_nuevo'),
    ]