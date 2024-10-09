from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.estudiante.models.estudiante import Estudiante
from apps.materia.models.materia import Materia


class Nota(models.Model):
    CORTE_CHOICES = [
        (1, 'Corte 1'),
        (2, 'Corte 2'),
        (3, 'Corte 3'),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    corte = models.IntegerField(choices=CORTE_CHOICES)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0)
    ])

    class Meta:
        db_table = 'nota'
        unique_together = ('estudiante', 'materia', 'corte')

    def __str__(self):
        return f'{self.estudiante} - {self.materia} - Corte {self.corte}: {self.calificacion}'
