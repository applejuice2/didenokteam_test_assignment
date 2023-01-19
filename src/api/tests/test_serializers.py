from django.test import TestCase

from api.serializers import ServiceSerializer
from services.models import Service
from api.utils import encrypt


class ServiceSerializerTests(TestCase):
    def test_serializer(self):
        """Тестирует сериализатор с несколькими """
        """экземплярами модели."""
        service_1 = Service.objects.create(
            service_name='yundexorpf',
            password=encrypt('Password1'),
        )
        service_2 = Service.objects.create(
            service_name='yunsfkkcvck',
            password=encrypt('Password2'),
        )

        data = ServiceSerializer(
            (service_1, service_2), many=True
        ).data
        expected_data = (
            {
                'service_name': 'yundexorpf',
                'password': 'Password1'
            },
            {
                'service_name': 'yunsfkkcvck',
                'password': 'Password2'
            }
        )

        self.assertEqual(expected_data, (dict(data[0]), dict(data[1]),))

    def test_serializer_password_validation(self):
        """Тестирует сериализатор при """
        """невалидном пароле."""
        service_1 = Service.objects.create(
            service_name='yundexorpf',
            password=encrypt('ccjjhfejfehfHDHF7s'),
        )

        serializer = ServiceSerializer(data=service_1)
        self.assertEqual(serializer.is_valid(), False)
