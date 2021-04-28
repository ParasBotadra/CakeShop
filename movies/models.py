from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    poster = models.ImageField(null=True, blank=True, upload_to='movies/')
    released_on = models.DateField()
    genre = models.CharField(max_length=250)
    director = models.CharField(max_length=250)

    def __str__(self):
        return self.title
