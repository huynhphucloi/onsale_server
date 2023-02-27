from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ShopGroup(models.Model):
    name = models.CharField(max_length=25, default="List shop Name")
    password = models.CharField(max_length=7, default="Password for list shop", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Shop Groups"


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=25, default="Shop Name")
    url = models.CharField(max_length=500, default="Link Website for Shop")
    password = models.CharField(max_length=7, default="Password add Shop", unique=True)
    open_hour = models.IntegerField(default=8, validators=[
        MinValueValidator(0, message="Opening time must be between 0h and 23h"),
        MaxValueValidator(23, message="Opening time must be between 0h and 23h")
    ])
    close_hour = models.IntegerField(default=20, validators=[
        MaxValueValidator(24, message="The latest closing time is 24h"),
        MinValueValidator(1, message="Closing time must be at least 1 hour longer than opening time")
    ])
    message = models.CharField(max_length=150, default="Message notification")
    message_two = models.CharField(max_length=150, default="Message notification 0m Distance")
    google_maps = models.CharField(max_length=600, default="Link Google Maps")
    lat = models.FloatField(max_length=10, default=0.0)
    lng = models.FloatField(max_length=10, default=0.0)
    distance = models.IntegerField(default=150)
    shop_group = models.ForeignKey(ShopGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_group.name

    def json(self):
        return {
            "name": self.name,
            "url": self.url,
            "open_hour": self.open_hour,
            "close_hour": self.close_hour,
            "information": {
                "messageOne": self.message,
                "messageTwo": self.message_two,
                "lat": self.lat,
                "lng": self.lng,
                "distance": self.distance
            },
        }
