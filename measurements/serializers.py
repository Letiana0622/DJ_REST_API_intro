# TODO: опишите сериализаторы

from rest_framework import serializers

from measurements.models import Project, Measurement

class SensorSerializer(serializers.ModelSerializer):

    # name = serializers.CharField(min_length=7)

    class Meta:
        model = Project
        fields = ['id','name','latitude','longitude', 'created_at','updated_at']


class SensorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
        # fields = ['project', 'value','created_at','updated_at'] # Поле project и есть id sensor (=project_id)
