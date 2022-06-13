from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=50)
	release_date = models.DateField()

class Song(models.Model):
	name = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)