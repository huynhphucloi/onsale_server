from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Shop, ShopGroup
import json


# Create your views here.
def get_shop(request):
    try:
        list_shop_id = request.GET.get("list_shop_id")
        item = ShopGroup.objects.get(password=list_shop_id)
        list_shop = item.shop_set.all()
        data = serializers.serialize("json", list_shop)
        return HttpResponse(
            data, content_type="application/json"
        )
    except Shop.DoesNotExist:
        return JsonResponse(
            {
                "error": 404,
                "message": "List shop Not Found"
            }
        )


def validate_shop(request):
    try:
        shop_id = request.GET.get("shop_id")
        item = Shop.objects.get(password=shop_id)
        return HttpResponse(
            status=200
        )
    except Shop.DoesNotExist:
        return HttpResponse(
            status=404
        )
