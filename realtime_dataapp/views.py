from django.shortcuts import render

# Create your views here.
import threading
def realtimeshow(request):
    print('we are here in realtimeshow views')

    print('we are ready to start our pub server')

    return render(request, 'sinexamplequater.html')
