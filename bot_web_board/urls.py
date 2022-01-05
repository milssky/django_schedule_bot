from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index_bot),
    path('', views.tg_login)
]
