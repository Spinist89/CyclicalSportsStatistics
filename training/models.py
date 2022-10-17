from django.db import models


class Training(models.Model):
    main_tasks = models.CharField(max_length=32)
    # coach = models.ManyToManyField()
    # sportsmen = models.ManyToManyField()
    # intermediate_result = models.IntegerField()


class Result(models.Model):
    # coach = models.ManyToManyField()
    # sportsmen = models.ManyToManyField()
    # group = models.ManyToManyField()
    # training = models.ManyToManyField()
    updated_at = models.DateTimeField(auto_now=True)
    average_result = models.IntegerField()
