from django.urls import path
from realtime_dataapp.views import realtimeshow,realtimeshowmulti

urlpatterns = [
    path('realtimeshow', realtimeshow, name='send-url'),
    path('realtimeshowmulti', realtimeshowmulti, name='send-url')
]