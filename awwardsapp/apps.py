from django.apps import AppConfig


class AwwardsAppConfig(AppConfig):
    name = 'awwardsapp'

    def ready(self):
        import awwardsapp.signals

