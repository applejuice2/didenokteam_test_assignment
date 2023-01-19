import re

from rest_framework import serializers

from services.models import Service
from .utils import encrypt, decrypt


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'service_name', 'password',
        )
        read_only_fields = ('service_name',)

    def validate_password(self, value):
        if not re.match((r'^(?=^.{8,50}$)((?=.*\d)|(?=.*\W+))'
                         r'(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$\Z'), value):
            raise serializers.ValidationError(
                'Минимум 8 символов (максимум 50): '
                'одна цифра, одна буква в верхнем регистре и одна в нижнем'
            )
        return value

    def create(self, validated_data):
        service_name = validated_data['service_name']
        password = validated_data['password']
        encrypted_password = encrypt(password)
        service, _ = (
            Service
            .objects
            .update_or_create(service_name=service_name,
                              defaults={'password': encrypted_password})
        )
        return service

    def to_representation(self, data):
        data = super(ServiceSerializer, self).to_representation(data)
        data['password'] = decrypt(data['password'])
        return data
