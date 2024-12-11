from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theProject2.users'

    def ready(self):
        import theProject2.users.signals