from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.home, name='home'),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso)
]