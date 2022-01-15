import logging
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

logging.basicConfig(level=logging.DEBUG)

# Create your views here.
def index_bot(request):
    logging.info('index')
    return render(request, 'bot_web_board/tg_login.html')


def tg_login(request):
    logging.info("Login detected")
    logging.info(request)
    return HttpResponsePermanentRedirect('/')
