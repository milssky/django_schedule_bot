import hashlib
import hmac
from hashlib import sha256

from django.conf import settings


def validate_auth_data(auth_data: dict) -> bool:
    """ Проверяет запрос, полученный от серверов TG на достоверность. """
    tg_hash = auth_data['hash']
    auth_data.pop('hash')
    auth_data = sorted(auth_data.items())
    data_check_string = '\n'.join(map(lambda x: '='.join(x), auth_data))
    secret_key = sha256(settings.BOT_API_TOKEN.encode('utf-8')).digest()
    check_message = bytearray(data_check_string, 'utf-8')
    data_hash = hmac.new(secret_key, msg=check_message, digestmod=hashlib.sha256).hexdigest()
    return data_hash == tg_hash
