from django.shortcuts import render

# Create your views here.

def getfrom(request):
    return render(request, 'message_form.html')