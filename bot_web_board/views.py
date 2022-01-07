from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect


# Create your views here.
def index_bot(request):
    return render(request, 'bot_web_board/tg_login.html')


def tg_login(request):
    print(request)
    return HttpResponsePermanentRedirect('/')
