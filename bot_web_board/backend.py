from django.contrib.auth.backends import BaseBackend


class TelegramBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        pass

    def get_user(self, user_id):
        pass
