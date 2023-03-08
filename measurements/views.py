from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from .models import Project, Measurement
from .serializers import SensorSerializer, SensorDetailsSerializer
from rest_framework.response import Response

# Необходимо реализовать REST API для создания/получения/обновления/удаления показания температуры.

class AddListSensorView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = SensorSerializer
    queryset = Project.objects.all()

    def perform_create(self, serializer):
        project = get_object_or_404(Project, id=self.request.data.get('id'))
        serializer.save(project=project)

# class ListSensorView(generics.ListAPIView):
#     queryset = Project.objects.filter(draft=False)
#     serializer_class = SensorSerializer

class RetrieveUpdateDestroySensorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorSerializer
    queryset = Project.objects.all()


class AddListSensorDetailView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = SensorDetailsSerializer
    queryset = Measurement.objects.all()

    def perform_create(self, serializer):
        measurement = get_object_or_404(Measurement, id=self.request.data.get('id'))
        serializer.save(measurement=measurement)


# class ListSensorDetailView(generics.ListAPIView):
#     serializer_class = SensorDetailsSerializer
#     queryset = Measurement.objects.all()

class RetrieveUpdateDestroySensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorDetailsSerializer
    queryset = Measurement.objects.all()
