from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField("Название группы", max_length=32)
    coach = models.ForeignKey(User, related_name="group", on_delete=models.SET_NULL, null=True)
    sportsmen = models.ManyToManyField(User, related_name="group1")

    # training = models.ForeignKey()
    created_at = models.DateTimeField("Вркемя создания", auto_now_add=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


