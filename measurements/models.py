from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    # - датчик:
    # - название
    # - описание(необязательное, например, "спальня"
    # "корридор на 2 этаже")

    name = models.TextField()
    description = models.TextField()

class Measurement(models.Model):
    # - измерение температуры:
    # - ID датчика
    # - температура при измерении
    # - дата измерения

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
