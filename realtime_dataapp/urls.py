from django.urls import path
from realtime_dataapp.views import realtimeshow,realtimeshowmulti,fast_display

urlpatterns = [
    path('realtimeshow', realtimeshow, name='send-url'),
    path('realtimeshowmulti', realtimeshowmulti, name='send-url'),
path('fastdisplay', fast_display, name='send-url'),
]