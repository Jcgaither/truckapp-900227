from django.apps import AppConfig
from actstream import registry

class MyAppConfig(AppConfig):
    name = 'trucks'

    def ready(self):
        registry.register(self.get_model('trucks'))

