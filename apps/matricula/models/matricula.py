from django.db import models
from apps.estudiante.models.estudiante import Estudiante
from apps.materia.models.materia import Materia
from apps.nota.models.nota import Nota


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'matricula'
        unique_together = ('estudiante', 'materia')

    def calcular_nota_final(self):
        notas = Nota.objects.filter(estudiante=self.estudiante, materia=self.materia)
        if notas.count() == 0:
            return 0.0
        return sum([nota.calificacion for nota in notas]) / notas.count()

    def save(self, *args, **kwargs):
        self.nota_final = self.calcular_nota_final()
        super(Matricula, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.estudiante} - {self.materia} - Nota final: {self.nota_final}'
