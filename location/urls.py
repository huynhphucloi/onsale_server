from django.urls import path
from .views import get_shop, shop, loginPage, logoutPage


urlpatterns = [
    path('login/', loginPage, name='login_register'),
    path('logout/', logoutPage, name='logout'),
    path('get_shop/', get_shop, name="get_shop"),
    path('shop/', shop, name="shop"),
]
