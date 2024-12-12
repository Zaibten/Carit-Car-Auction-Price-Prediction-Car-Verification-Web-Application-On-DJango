import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack  # Add this line
import app.routing as route  # Make sure you're importing from the correct module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AutoTrader.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(  # Wrap with AuthMiddlewareStack
        URLRouter(
            route.websocket_urlpatterns
        )
    ),
})
