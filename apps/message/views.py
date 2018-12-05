from django.shortcuts import render

from .models import UserMessage
# Create your views here.

def getfrom(request):
    # all_messages = UserMessage.objects.all()
    all_messages = UserMessage.objects.filter(name='sunday_test', address='北京')
    for magssage in all_messages:
        print(magssage.name)
    return render(request, 'message_form.html')