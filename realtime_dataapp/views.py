from django.shortcuts import render

# Create your views here.

def realtimeshow(request):
    print('we are here in realtimeshow views')
    return render(request, 'sinexample.html')
