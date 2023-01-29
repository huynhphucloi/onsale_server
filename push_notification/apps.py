from django.apps import AppConfig


class PushNotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'push_notification'

    # def ready(self):
    #     import push_notification.signals
