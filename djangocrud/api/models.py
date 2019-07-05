from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models. CharField(max_length=256)
    year = models.IntegerField()
    num = models.IntegerField()


class Movie1(models.Model):
    title = models.CharField(max_length=32)
    desc = models. CharField(max_length=256)
    year = models.IntegerField()
    num = models.IntegerField()


class Users(models.Model):
    user_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
