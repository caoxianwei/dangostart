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
    # user_message = UserMessage()
    # user_message.name = 'bbb'
    # user_message.message = '新加test'
    # user_message.address = '杭州'
    # user_message.email = 'bbb@tt.com'
    # user_message.object_id = 'bbb1'
    # user_message.save()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = name
        user_message.save()

    return render(request, 'message_form.html')

def deletefrom(request):
    all_messages = UserMessage.objects.filter(name='sunday')
    for massage in all_messages:
        print(massage.name)
        massage.delete()
    return render(request, 'message_form.html')

def getDetail(request, detail_id):
    print(detail_id)
    message = None
    all_messages = UserMessage.objects.filter(name=detail_id)
    if all_messages:
        message = all_messages[0]
    return render(request, 'message_form.html', {
        'message': message
    })