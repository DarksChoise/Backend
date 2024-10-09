from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from apps.materia.models.materia import Materia
from apps.materia.serializers.materia_serializer import MateriaSerializer


class MateriaViewSet(viewsets.GenericViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    def create(self, request):
        """
        Handle the creation of a new Materia instance.

        This method uses a serializer to validate and save the incoming data from the request.
        If the data is valid, a new Materia instance is created and a response with the 
        serialized data is returned with a status of HTTP 201 Created.

        Args:
            request (Request): The HTTP request object containing the data to be serialized.

        Returns:
            Response: A response object containing the serialized data of the newly created 
            Materia instance and an HTTP 201 Created status.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        Retrieves a list of subject records.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A Response object containing serialized subject data.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single Materia instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Materia instance to retrieve.

        Returns:
            Response: A Response object containing the serialized data of the retrieved Materia instance.
        """
        queryset = self.get_queryset()
        materia = queryset.get(pk=pk)
        serializer = self.get_serializer(materia)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a Materia instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Materia instance to update.

        Returns:
            Response: A Response object containing the serialized data of the updated Materia instance.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Delete a Materia instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Materia instance to delete.

        Returns:
            Response: A Response object with an HTTP 204 No Content status.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
