from django.db import models

# Create your models here.

class Sample(models.Model):
    num = models.PositiveIntegerField()
    num_2 = models.PositiveIntegerField()

class Sample_1(models.Model):
    balance = models.PositiveIntegerField()

class Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    count = models.PositiveIntegerField()

class Account(models.Model):
    name = models.CharField(max_length = 100)
    balance = models.PositiveIntegerField()


