from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser



# User = get_user_model()


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'sportsmen'),
        (2, 'coach'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)






# class Coach(models.Model):
#     surname = models.CharField(max_length = 32)
#     name = models.CharField(max_length = 32)
#     patronymic = models.CharField(max_length = 32, null=True)
#     login = models.CharField(max_length = 32)
#     password = models.CharField(max_length = 32)
#     email = models.EmailField(max_length = 254)
#     # sport_type = models.ManyToManyField()
#     # sportsmen = models.ManyToManyField()
#     # group = models.ManyToManyField()
#     # training = models.ManyToManyField()
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add = True)
#
# class Sportsmen(models.Model):
#     surname = models.CharField(max_length=32)
#     name = models.CharField(max_length=32)
#     patronymic = models.CharField(max_length=32, null=True)
#     login = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     email = models.EmailField(max_length=254)
#     # sport_type = models.ManyToManyField()
#     # group = models.ManyToManyField()
#     # training = models.ManyToManyField()
#     # coach = models.ManyToManyField()
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)

