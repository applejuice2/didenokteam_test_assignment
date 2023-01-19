from http import HTTPStatus

from rest_framework.test import APITestCase

from services.models import Service
from api.utils import encrypt
from api.serializers import ServiceSerializer


class ServiceAPITests(APITestCase):
    def test_api_from_existed_service_name(self):
        """Страница c URL по имени сервиса отображается"""
        """любому пользователю после создания экземпляра модели."""
        service_1 = Service.objects.create(
            service_name='test1_',
            password=encrypt('Password1'),
        )
        url = '/password/test1_/'

        response = self.client.get(url)
        serializer_data = ServiceSerializer(service_1).data

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(serializer_data, response.data)

    def test_api_with_filter_service_name(self):
        """Страница c URL по части имени сервиса"""
        """возвращает сервис/ы"""
        service_1 = Service.objects.create(
            service_name='yundexorpf',
            password=encrypt('Password1'),
        )
        service_2 = Service.objects.create(
            service_name='yunsfkkcvck',
            password=encrypt('Password2'),
        )
        url = '/password/?service_name=yun'

        response = self.client.get(url)
        serializer_data = ServiceSerializer(
            [service_1, service_2], many=True
        ).data

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(serializer_data, response.data)
