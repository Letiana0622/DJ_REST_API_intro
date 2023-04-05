# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer
from rest_framework.response import Response

class AddListSensorView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('id'))
        serializer.save(sensor=sensor)

class RetrieveUpdateDestroySensorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

class AddListMeasurementView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

    def perform_create(self, serializer):
        measurement = get_object_or_404(Measurement, id=self.request.data.get('id'))
        serializer.save(measurement=measurement)

class RetrieveUpdateDestroyMeasurementView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()


class ListSensorDetailView(generics.ListAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()


