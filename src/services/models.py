from django.db import models
from django.core.validators import RegexValidator


class Service(models.Model):
    service_name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя сервиса',
        help_text=(
            'Обязательное поле. Не более 150 символов. '
            'Только буквы, цифры и @/./+/-/_ .'
        ),
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message='Некоторые символы не поддерживаются',
            ),
        ],
        error_messages={
            "unique": ('Сервис с таким названием уже существует'),
        },
    )
    password = models.CharField(
        max_length=250,
        verbose_name='Пароль от сервиса в зашифрованном виде'
    )

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
        ordering = ['service_name']

    def __str__(self):
        return self.service_name
