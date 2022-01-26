import logging
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

from .logic import validate_auth_data

logging.basicConfig(level=logging.DEBUG)


def index_bot(request):
    return render(request, 'bot_web_board/tg_login.html')


def tg_login(request):
    auth_data = dict(request.GET.items())
    if not validate_auth_data(auth_data):
        logging.error(f'Wrong login with {auth_data}')
        return HttpResponse('Wrong auth data. Check it and try again')

    return HttpResponsePermanentRedirect('/')
