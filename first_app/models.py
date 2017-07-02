from django.db import models
from datetime import date


# Create your models here.
class Actors(models.Model):
    fullname = models.CharField(max_length=200)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=10)
    def __str__(self):
        return self.fullname

class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    actor  = models.ForeignKey(Actors)
    year  = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    movie_logo = models.CharField(max_length=200)
    def __str__(self):
        return self.movie_title
