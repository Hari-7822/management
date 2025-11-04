from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User = get_user_model()
class CustomAuthBackend(ModelBackend):
    """
    Authenticate using username/email with password or access_key (key).
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        key = kwargs.get('key')
        email = kwargs.get('email')
        user = None
        try:
            if username:
                user = User.objects.get(username=username)
            elif email:
                user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if user:
            if password and user.check_password(password):
                return user
            if key and user.access_key and check_password(key, user.access_key):
                return user
        return None
