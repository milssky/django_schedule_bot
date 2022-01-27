from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from .models import Task, TgUser


@sync_to_async
def get_user_tasks(user_id) -> str:
    """Подготавливает список задач для конкретного юзера."""
    tasks = Task.objects.filter(author__tg_user=user_id)
    return "\n".join([task.text for task in tasks])


@sync_to_async
def get_user_from_tg_id(tg_id) -> str:
    """Получает User из БД или возрвщает пустую строку в случае его отсутствия"""
    try:
        user = TgUser.objects.get(tg_user=tg_id)
    except ObjectDoesNotExist:
        return ""
    return user.username
