from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'password',)
    list_display_links = ('service_name',)
    search_fields = ('service_name',)


admin.site.register(Service, ServiceAdmin)
