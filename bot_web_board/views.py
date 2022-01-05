from django.shortcuts import render, HttpResponse


# Create your views here.
def index_bot(request):
    print(request)
    return HttpResponse("Hello")


def tg_login(request):
    print(request)
    return render(request, 'bot_web_board/tg_login.html')
