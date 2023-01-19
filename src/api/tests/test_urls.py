from http import HTTPStatus

from django.test import TestCase, Client

from services.models import Service
from api.utils import encrypt


class ServiceURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Service.objects.create(
            service_name='test-service_name',
            password=encrypt('jvmvmvmJFiC8'),
        )

    def setUp(self):
        self.guest_client = Client()

    def test_url_exists_at_desired_location(self):
        """Общая страница, страница по части имени сервиса, """
        """страница по имени сервиса доступны любому пользователю """
        """и существуют из-за создания тестового объекта."""
        urls = [
            '/password/',
            '/password/test-service_name/',
            '/password/?service_name=tes',
        ]
        for adress in urls:
            with self.subTest(adress=adress):
                response = self.client.get(adress)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_service_url_doesnt_exists_at_desired_location(self):
        """Страница /password/no_test/ не существует """
        """(объект под с service_name = no_test не создавался)"""
        response = self.guest_client.get('/password/no_test/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
