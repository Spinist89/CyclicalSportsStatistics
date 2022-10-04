from django.db import models

class Group(models.Model):
    main_tasks = models.CharField(max_length=32)
    # coach = models.ManyToManyField()
    # sportsmen = models.ManyToManyField()
    # statistics = models.IntegerField()