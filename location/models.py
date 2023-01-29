from django.db import models


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
    url = models.CharField(max_length=50, default="Link Website for Shop")
    password = models.CharField(max_length=7, default="Password add Shop", unique=True)
    open_hour = models.IntegerField(default=8)
    close_hour = models.IntegerField(default=20)
    message = models.CharField(max_length=150, default="Message notification")
    google_maps = models.CharField(max_length=300, default="Link Google Maps")
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
                "message": self.message,
                "lat": self.lat,
                "lng": self.lng,
                "distance": self.distance
            },
        }
