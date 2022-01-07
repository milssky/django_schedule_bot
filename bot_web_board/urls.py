from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_bot),
    path('tg_login/', views.tg_login)
]
