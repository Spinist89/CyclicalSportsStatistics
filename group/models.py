from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=32)
    # coach = models.ManyToManyField()
    # sportsmen = models.ManyToManyField()
    # training = models.ManyToManyField()
    created_at = models.DateTimeField(auto_now_add=True)
