from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task, TgUser

# Register your models here.
admin.site.register(TgUser, UserAdmin)
admin.site.register(Task)
