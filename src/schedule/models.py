from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.

class Date(models.Model):
	date = models.IntegerField()
	month = models.CharField(max_length=250)
	def __str__(self):
		return self.date

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)

	#primary/unique key; each album has one key
	#Red:pk=1

	#each song is linked to an album
	#fk=1 (so we know this song belongs to red)
	def __str__(self):
		return self.album_title
 #primary/unique key; each album has one key
 #Red:pk=1

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	def __str__(self):
		return self
 #each song is linked to an album
 #fk=1 (so we know this song belongs to red)

