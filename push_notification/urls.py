from .views import createNotification
from django.urls import path


urlpatterns = [
    path('create/', createNotification, name='create_notification'),
]
