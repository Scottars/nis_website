from django.shortcuts import render

def chat(request):
    print('we are in chat')
    return render(request, 'chat/room.html')

