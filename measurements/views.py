from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer
from rest_framework.response import Response

# Необходимо реализовать REST API для создания/получения/обновления/удаления показания температуры.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


    def create(self, request):
        return Response({'status': 'OK'})

    def list(self, request):
        serializer = Project.objects.all()
        serializer_class = ProjectSerializer(serializer, many=True)
        return Response(serializer_class.data)

    def update(self, request, pk=None):
        return Response({'status': 'OK'})

    def destroy(self, request, pk=None):
        return Response({'status': 'OK'})

    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass

class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

    def create(self, request):
        return Response({'status': 'OK'})

    def list(self, request):
        serializer = Measurement.objects.all()
        serializer_class = MeasurementSerializer(serializer, many=True)
        return Response(serializer_class.data)

    def update(self, request, pk=None):
        return Response({'status': 'OK'})

    def destroy(self, request, pk=None):
        return Response({'status': 'OK'})

    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
