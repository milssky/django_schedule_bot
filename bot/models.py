from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TgUser(AbstractUser):
    tg_user_id = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}:{self.tg_user_id}'


class Task(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    author = models.ForeignKey(TgUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.author} - {self.text} - {self.created_at}'

    class Meta:
        ordering = ("-created_at",)
