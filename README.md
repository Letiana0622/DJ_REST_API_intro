API CRUD
======

## Техническая задача: реализовать CRUD-логику, используя Django Rest Framework.

**CRUD** – аббревиатура для Create-Read-Update-Delete. Ей обозначают логику для операций создания-чтения-обновления-
удаления сущностей. Подробнее: https://ru.wikipedia.org/wiki/CRUD

## Описание

У нас есть программируемые датчики, измеряющие температуру. Раз в некоторый интервал времени датчики делают запрос по
API и записывают свои показания. В показания датчики передают ID объекта и текущую температуру в градусах Цельсия.

Необходимо реализовать REST API для создания/получения/обновления/удаления показания температуры.

Требуется задать 2 модели (они уже описаны в models.py):

- объект
    - название
    - координаты широты
    - координаты долготы
    - дата создания
    - дата обновления

- измерение температуры:
    - ID объекта
    - температура при измерении
    - дата создания измерения

Используйте `ViewSet` для описания всех API-ручек сущностей. Вам нужно будет завести 2 `ViewSet`'а: один для объекта,
и другой для измерения.

Документация для `ViewSet`: https://www.django-rest-framework.org/api-guide/viewsets/

Наследуйтесь от `ModelViewSet`, там уже реализована основная логика, вам потребуется правильно описать сериализаторы.

Для сериализаторов используйте `ModelSerializer`.

## Подсказки

1. Вам необходимо будет задать логику во views, urls и serializers. В места, где нужно добавлять код, включены 
2. `TODO`-комментарии. После того как вы добавите код, комментарии можно удалить.

2. Для автоматического проставления времени используйте аргументы: `auto_now` (при обновлении) и 
3. `auto_now_add` (при создании).
https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField

## Доп-задания

### Абстрактный класс для времени

Вынесите `created_at` / `updated_at` поля в отдельный абстрактный класс `TimestampFields`: https://docs.djangoproject.com/en/3.1/topics/db/models/#abstract-base-classes

**Вопрос:** на что при этом влияет флаг `abstract = True`? Как будет устроено наследование, если не указать этот параметр?

### Прикрепление картинки к измерению

Датчики стали более продвинутыми и могут также прикреплять снимки. Добавьте nullable-поле к модели `Measurement` 
для сохранения изображений https://www.django-rest-framework.org/api-guide/fields/#imagefield

Обратите внимание, что поле должно быть опциональным – некоторые датчики прикладывают фото, а некоторые нет. 
Для старых датчиков ничего не должно сломаться.

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Вам необходимо будет создать базу в postgres и прогнать миграции:

```base
manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```

