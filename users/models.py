from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USER_TYPE_CHOICES = (
        (1, 'sportsmen'),
        (2, 'coach'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    group = models.ForeignKey("Group", related_name="sportsmen", on_delete=models.SET_NULL, null=True)

class Group(models.Model):
    title = models.CharField("Название группы", max_length=32)
    coach = models.ForeignKey("User", related_name="opg", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("Время создания", auto_now_add=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title