from django.db import models


class Group(models.Model):
    title = models.CharField("Название группы", max_length=32)
    # coach = models.ManyToManyField()
    # sportsmen = models.ManyToManyField()
    # training = models.ManyToManyField()
    created_at = models.DateTimeField("Вркемя создания", auto_now_add=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title
