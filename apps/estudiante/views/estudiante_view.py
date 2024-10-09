from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.estudiante.models.estudiante import Estudiante
from apps.estudiante.serializers.estudiante_serializer import EstudianteSerializer


class EstudianteViewSet(viewsets.GenericViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    def create(self, request):
        """
        Handle the creation of a new Estudiante instance.

        This method uses a serializer to validate and save the incoming data from the request.
        If the data is valid, a new Estudiante instance is created and a response with the 
        serialized data is returned with a status of HTTP 201 Created.

        Args:
            request (Request): The HTTP request object containing the data to be serialized.

        Returns:
            Response: A response object containing the serialized data of the newly created 
            Estudiante instance and an HTTP 201 Created status.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        Retrieves a list of student records.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A Response object containing serialized student data.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single Estudiante instance by its primary key (pk).

        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the Estudiante instance to retrieve.

        Returns:
            Response: A Response object containing the serialized data of the retrieved Estudiante instance.
        """
        queryset = self.get_queryset()
        estudiante = queryset.get(pk=pk)
        serializer = self.get_serializer(estudiante)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Updates an existing 'estudiante' instance with the provided data.

        Args:
            request (Request): The HTTP request containing the data to update the 'estudiante' instance.
            pk (int, optional): The primary key of the 'estudiante' instance to update.

        Returns:
            Response: A Response object containing the serialized data of the updated 'estudiante' instance.
        """
        queryset = self.get_queryset()
        estudiante = queryset.get(pk=pk)
        serializer = self.get_serializer(estudiante, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Deletes an Estudiante instance.

        Args:
            request: The HTTP request object.
            pk (int, optional): The primary key of the Estudiante instance to be deleted.

        Returns:
            Response: An HTTP response with status 204 (No Content) indicating successful deletion.
        """
        queryset = self.get_queryset()
        estudiante = queryset.get(pk=pk)
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
