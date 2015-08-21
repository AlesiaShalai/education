from django.apps import AppConfig


class MyAppConfig(AppConfig):

    name = 'site3'

    def ready(self):
        from . import signals