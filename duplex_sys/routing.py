from django.urls import re_path

from duplex_sys.consumers import ArraySort

websocket_urlpatterns = [
    re_path(r'ws/sort', ArraySort.as_asgi()),
]
