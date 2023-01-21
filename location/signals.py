from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Shop
from .helper.firebase_fcm import updateShop, removeShop


@receiver(pre_save, sender=Shop)
def createShop(sender, instance, *args, **kwargs):
    data = instance.google_maps.split('/')
    location = data[6].replace("@", "").split(',')
    instance.lat = location[0]
    instance.lng = location[1]


@receiver(post_save, sender=Shop)
def updateShopToApp(sender, instance, *args, **kwargs):
    updateShop(instance.password)


@receiver(post_delete, sender=Shop)
def removeShopToApp(sender, instance, *args, **kwargs):
    removeShop(instance.password)
