from django.db import models


# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=250)
    message = models.CharField(max_length=350)
    image = models.CharField(max_length=350)
    topic = models.CharField(max_length=350)

    def __str__(self):
        return self.title

