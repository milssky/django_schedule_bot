from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


# TODO нужна модель для юзера с хешем
class TelegramBackend(BaseBackend):
    def authenticate(self, request, username=None, hash=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
