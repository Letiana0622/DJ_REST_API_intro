"""simple_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from measurements.views import ProjectViewSet, MeasurementViewSet

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`

from measurements.views import AddListSensorView, AddListSensorDetailView
from measurements.views import RetrieveUpdateDestroySensorView, RetrieveUpdateDestroySensorDetailView

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'projects', ProjectViewSet, basename='project')
# router.register(r'measurements', MeasurementViewSet, basename='measurement')
# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensor/', AddListSensorView.as_view()),
    path('sensordetail/', AddListSensorDetailView.as_view()),
    path('changesensor/<pk>/', RetrieveUpdateDestroySensorView.as_view()),
    path('changesensordetail/<pk>/', RetrieveUpdateDestroySensorDetailView.as_view()),
]
              # +router.urls
