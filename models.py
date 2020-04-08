from django.db import models

# Create your models here.


class Streamer(models.Model):
    name = models.CharField(max_length=150)
    details = models.TextField()
    url = models.CharField(max_length=300)
    movies = models.FileField(upload_to='movie')

    def __str__(self):
        return self.name


class MovieName(models.Model):
    name = models.CharField(max_length=500)
    streamer = models.ForeignKey(to=Streamer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
