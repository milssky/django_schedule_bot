from django.urls import path
from . import views


app_name = 'web_board'

urlpatterns = [
    path('', views.index_bot),
    path('tg_login/', views.tg_login_callback),
    path('home/', views.home)
]
