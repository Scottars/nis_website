from django.urls import path
from realtime_dataapp.consumer import syncrealtimetConsumer,realtimeshow_Consumer

'''
    这个routing 就相当于django框架中的urls 文件，所有关于ws/chat的内容，我们都交给chatsonsumer进行处理
'''

websocket_urlpatterns = [
    path('ws/realtimeshow/', realtimeshow_Consumer),
]