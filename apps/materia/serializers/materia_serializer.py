from rest_framework import serializers

from apps.materia.models.materia import Materia


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
