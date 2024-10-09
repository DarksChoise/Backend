from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from apps.nota.models.nota import Nota
from apps.nota.serializers.nota_serializer import NotaSerializer


class NotaViewSet(viewsets.GenericViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    def create(self, request):
        """
        Handle the creation of a new Nota instance.

        This method uses a serializer to validate and save the incoming data from the request.
        If the data is valid, a new Nota instance is created and a response with the 
        serialized data is returned with a status of HTTP 201 Created.

        Args:
            request (Request): The HTTP request object containing the data to be serialized.

        Returns:
            Response: A response object containing the serialized data of the newly created 
            Nota instance and an HTTP 201 Created status.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        Retrieves a list of note records.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A Response object containing serialized note data.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single Nota instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Nota instance to retrieve.

        Returns:
            Response: A Response object containing the serialized data of the retrieved Nota instance.
        """
        queryset = self.get_queryset()
        nota = queryset.get(pk=pk)
        serializer = self.get_serializer(nota)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a single Nota instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Nota instance to update.

        Returns:
            Response: A Response object containing the serialized data of the updated Nota instance.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Delete a single Nota instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Nota instance to delete.

        Returns:
            Response: A Response object containing the serialized data of the deleted Nota instance.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
