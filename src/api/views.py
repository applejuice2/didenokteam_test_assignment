from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from services.models import Service
from .serializers import ServiceSerializer
from .mixins import ListViewSet
from .filters import ServiceFilter
from .validators import validate_service_name


class ServiceViewSet(ListViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = (ServiceFilter,)
    search_fields = ('service_name',)

    @action(methods=['get', 'post', ],
            detail=False,
            url_path=r'(?P<service_name>[\s\S]+)',)
    def get_or_create_service_password(self, request, service_name):
        if request.method == 'GET':
            service = get_object_or_404(Service, service_name=service_name)
            serializer = self.get_serializer(service)
            return Response(serializer.data)

        if not validate_service_name(service_name):
            return Response(
                {'service_name': ('Не более 150 символов. '
                                  'Только буквы, цифры и @/./+/-/_ .')},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(service_name=service_name)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)
