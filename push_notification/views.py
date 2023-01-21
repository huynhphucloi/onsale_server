from django.shortcuts import HttpResponse
import json
from .models import Notification
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def createNotification(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            notification = Notification(title=json_data["title"], message=json_data["message"],
                                        topic=json_data["topic"], image=json_data["image"])
            notification.save()
            return HttpResponse("ok")
        except:
            return HttpResponse("false")
