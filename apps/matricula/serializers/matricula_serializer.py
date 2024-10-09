from rest_framework import serializers

from apps.matricula.models.matricula import Matricula


class MatriculaSerializer(serializers.ModelSerializer):
    nota_final = serializers.FloatField(read_only=True)

    class Meta:
        model = Matricula
        fields = [
            'id',
            'materia',
            'estudiante',
            'nota_final'
        ]
