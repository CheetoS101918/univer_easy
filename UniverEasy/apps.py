from django.apps import AppConfig


class UnivereasyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UniverEasy'


    class Meta:
        app_label = 'UniverEasy'
