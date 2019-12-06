from django.urls import path
from realtime_dataapp.views import realtimeshow

urlpatterns = [
    path('realtimeshow', realtimeshow, name='send-url')
]