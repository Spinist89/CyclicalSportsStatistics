from django.db import models


class Coach(models):
    surname = models.CharField(max_length = 32)
    name = models.CharField(max_length = 32)
    patronymic = models.CharField(max_length = 32, null=True)
    login = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
    email = models.EmailField(max_length = 254)
    # sport_type = models.ManyToManyField()
    # sportsmen = models.ManyToManyField()
    # group = models.ManyToManyField()
    # training = models.ManyToManyField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add = True)

class Sportsmen(models):
    surname = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32, null=True)
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    # sport_type = models.ManyToManyField()
    # group = models.ManyToManyField()
    # training = models.ManyToManyField()
    # coach = models.ManyToManyField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

