from rest_framework import serializers

# TODO: опишите необходимые сериализаторы


from rest_framework import serializers

from measurements.models import Sensor, Measurement



class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at','updated_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['name', 'description', 'measurement']
