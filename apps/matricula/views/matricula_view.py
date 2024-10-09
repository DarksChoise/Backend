from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from apps.matricula.models.matricula import Matricula
from apps.matricula.serializers.matricula_serializer import MatriculaSerializer


class MatriculaViewSet(viewsets.GenericViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    def create(self, request):
        """
        Handle the creation of a new Matricula instance.

        This method uses a serializer to validate and save the incoming data from the request.
        If the data is valid, a new Matricula instance is created and a response with the 
        serialized data is returned with a status of HTTP 201 Created.

        Args:
            request (Request): The HTTP request object containing the data to be serialized.

        Returns:
            Response: A response object containing the serialized data of the newly created 
            Matricula instance and an HTTP 201 Created status.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        Retrieves a list of matricula records.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A Response object containing serialized matricula data.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single Matricula instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Matricula instance to retrieve.

        Returns:
            Response: A Response object containing the serialized data of the retrieved Matricula instance.
        """
        queryset = self.get_queryset()
        matricula = queryset.get(pk=pk)
        serializer = self.get_serializer(matricula)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a Matricula instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Matricula instance to update.

        Returns:
            Response: A Response object containing the serialized data of the updated Matricula instance.
        """
        queryset = self.get_queryset()
        matricula = queryset.get(pk=pk)
        serializer = self.get_serializer(matricula, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Delete a Matricula instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Matricula instance to delete.

        Returns:
            Response: A Response object containing the serialized data of the deleted Matricula instance.
        """
        queryset = self.get_queryset()
        matricula = queryset.get(pk=pk)
        serializer = self.get_serializer(matricula)
        matricula.delete()
        return Response(serializer.data)
