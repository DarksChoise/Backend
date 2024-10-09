from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.materia.views.materia_view import MateriaViewSet
from apps.estudiante.views.estudiante_view import EstudianteViewSet
from apps.nota.views.nota_view import NotaViewSet
from apps.matricula.views.matricula_view import MatriculaViewSet

router = DefaultRouter()

router.register('materias', MateriaViewSet, basename='materia')
router.register('estudiantes', EstudianteViewSet, basename='estudiante')
router.register('notas', NotaViewSet, basename='nota')
router.register('matriculas', MatriculaViewSet, basename='matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
