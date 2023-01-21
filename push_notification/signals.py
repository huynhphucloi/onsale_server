from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from location.helper.firebase_fcm import sendNotification


@receiver(post_save, sender=Notification)
def updateShopToApp(sender, instance, created, **kwargs):
    # updateShop(instance.password)
    print("Created status", created)
    if created:
        sendNotification(instance)

