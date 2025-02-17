from rest_framework import serializers

from apps.estudiante.models.estudiante import Estudiante


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
