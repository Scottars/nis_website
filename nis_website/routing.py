from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import realtime_dataapp.routing
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    # 普通的HTTP请求不需要我们手动在这里添加，框架会自动加载过来
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns,
        )
    ),
    # 'websocket': AuthMiddlewareStack(
    #     URLRouter(
    #         realtime_dataapp.routing.websocket_urlpatterns
    #     )
    # ),

})