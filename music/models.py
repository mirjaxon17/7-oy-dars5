from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)


class Album(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)

class Song(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)




