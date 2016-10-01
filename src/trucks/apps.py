from django.apps import AppConfig
from actstream import registry
from django.contrib.auth import get_user_model
from django.conf import settings

User = settings.AUTH_USER_MODEL


class MyAppConfig(AppConfig):
    name = 'trucks'

    def ready(self):
        registry.register(User, self.get_model('PlusTruck'))



# myapp/__init__.py

# default_app_config = 'trucks.apps.MyAppConfig'