from .models import Task, User
from django.core.exceptions import ObjectDoesNotExist


def get_user_tasks(user_id) -> str:
    """Подготавливает список задач для конкретного юзера."""
    tasks = Task.objects.filter(author__tg_user_id=user_id)
    return "\n".join([task.text for task in tasks])


def get_user_from_tg_id(tg_id) -> str:
    """Получает User из БД или возрвщает пустую строку в случае его отсутствия"""
    try:
        user = User.objects.get(tg_user_id=tg_id)
    except ObjectDoesNotExist:
        return ""
    return user.username
