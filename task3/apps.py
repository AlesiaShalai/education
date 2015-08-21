from django.apps import AppConfig


class MyAppConfig(AppConfig):

    name = 'task3'

    def ready(self):
        print('ready called!\n\n\n')

        from . import signals