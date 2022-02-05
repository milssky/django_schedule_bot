import logging
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect


from .utils import validate_auth_data

logging.basicConfig(level=logging.ERROR)


def index_bot(request):
    return render(request, 'bot_web_board/tg_login.html')


def tg_login(request):
    auth_data = dict(request.GET.items())
    if not validate_auth_data(auth_data):
        logging.error(f'Wrong login with {auth_data}')
        return HttpResponse('Wrong auth data. Check it and try again')
    user = authenticate(username=auth_data['username'])
    login(request, user)
    return HttpResponsePermanentRedirect('/home')


@login_required
def home(request):
    user = request.user
    return HttpResponse(f'{user} logged in.')

