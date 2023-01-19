from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import ServiceViewSet

app_name = 'api'

router = DefaultRouter()
router.register('password', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]
