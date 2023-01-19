from django.test import TestCase

from services.models import Service


class ServiceModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = Service.objects.create(
            service_name='yundex',
            password='very_secret_pass'
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        service = ServiceModelTest.service
        field_verboses = {
            'service_name': 'Имя сервиса',
            'password': 'Пароль от сервиса в зашифрованном виде',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    service._meta.get_field(field).verbose_name, expected_value
                )

    def test_service_name_help_text(self):
        """help_text поля service_name совпадает с ожидаемым."""
        service = ServiceModelTest.service
        help_text = service._meta.get_field('service_name').help_text
        self.assertEqual(help_text, ('Обязательное поле. Не более '
                                     '150 символов. Только '
                                     'буквы, цифры и @/./+/-/_ .'))

    def test_object_name_is_title_fild(self):
        """__str__  - строчка с содержимым service.service_name."""
        service = ServiceModelTest.service
        expected_object_name = service.service_name
        self.assertEqual(expected_object_name, str(service))
