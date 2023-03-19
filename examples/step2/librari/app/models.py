from django.db import models
from uuid import uuid4


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()


class User(models.Model):
    first_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(max_length=64, unique=True)


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.ManyToManyField(Author)


class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, models.PROTECT)