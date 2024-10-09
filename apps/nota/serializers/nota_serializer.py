from rest_framework import serializers

from apps.nota.models.nota import Nota
from apps.estudiante.serializers.estudiante_serializer import EstudianteSerializer
from apps.materia.serializers.materia_serializer import MateriaSerializer


class NotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nota
        fields = [
            'id',
            'estudiante',
            'materia',
            'corte',
            'calificacion'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['estudiante'] = EstudianteSerializer(instance.estudiante).data
        representation['materia'] = MateriaSerializer(instance.materia).data
        return representation
