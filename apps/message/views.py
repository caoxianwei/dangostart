from django.shortcuts import render

from .models import UserMessage
# Create your views here.

def getfrom(request):
    # all_messages = UserMessage.objects.all()
    all_messages = UserMessage.objects.filter(name='sunday_test', address='北京')
    for magssage in all_messages:
        print(magssage.name)
    return render(request, 'message_form.html')

def addfrom(request):
    user_message = UserMessage()
    user_message.name = 'bbb'
    user_message.message = '新加test'
    user_message.address = '杭州'
    user_message.email = 'bbb@tt.com'
    user_message.object_id = 'bbb1'
    user_message.save()
    return render(request, 'message_form.html')