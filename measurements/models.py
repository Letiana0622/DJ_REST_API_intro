from django.db import models

# m1
class Project(models.Model):
    """Объект на котором проводят измерения."""
    #
    # - название
    # - координаты широты
    # - координаты долготы
    # - дата создания
    # - датаобновления

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class Measurement(models.Model):
    """Измерение температуры на объекте."""
    # - ID объекта
    # - температура при измерении
    # - дата создания измерения

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
