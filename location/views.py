from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Shop


# Create your views here.
def get_shop(request):
    try:
        shop_id = request.GET.get("shop_id")
        item = Shop.objects.get(password=shop_id)
        return JsonResponse(item.json(), )
    except Shop.DoesNotExist:
        return JsonResponse(
            {
                "error": 404,
                "message": "Shop Not Found"
            }
        )


@login_required(login_url='login_register')
def shop(request):
    user = request.user
    item = Shop.objects.get(user=user)
    if request.method == 'POST':
        item.name = request.POST.get("name")
        item.url = request.POST.get("url")
        item.password = request.POST.get("password")
        item.open_hour = request.POST.get("open_hour")
        item.close_hour = request.POST.get("close_hour")
        item.message = request.POST.get("message")
        item.lat = request.POST.get("latitude")
        item.lng = request.POST.get("longitude")
        item.distance = request.POST.get("distance")
        item.save()
        context = {"status": True}
        return render(request, 'location/update_page.html', context)
    context = {"shop": item, "status": False}
    return render(request, 'location/shop.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('shop')

    return render(request, 'location/login_register.html')


def logoutPage(request):
    logout(request)
    return redirect('login_register')
