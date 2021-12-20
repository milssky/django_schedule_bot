from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    tg_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username}:{self.tg_user_id}'


class Task(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.author} - {self.text} - {self.created_at}'

    class Meta:
        ordering = ("-created_at",)
