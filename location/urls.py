from django.urls import path
from .views import get_shop, validate_shop


urlpatterns = [
    path('get_shop/', get_shop, name="get_shop"),
    path('validate_shop/', validate_shop, name="validate_shop")
]
