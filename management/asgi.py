import os
from channels.routing import ProtocolTypeRouter

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')
students = get_asgi_application()

chat_app = ProtocolTypeRouter({
    "http": students,
})