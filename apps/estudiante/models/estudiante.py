from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField()

    class Meta:
        db_table = 'estudiante'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
