from django.db import models


class Training(models.Model):
    main_tasks = models.CharField(max_length=32)
    # coach = models.ManyToManyField()
    # sportsmen = models.ManyToManyField()
    # statistics = models.IntegerField()
    training_date = models.DateTimeField()
    result = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
