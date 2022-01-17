from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class TelegramBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        login_valid = (username == 'milssky')
        pwd_valid = True
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
