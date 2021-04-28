from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(null=True, blank=True)
    updated = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.author.name
