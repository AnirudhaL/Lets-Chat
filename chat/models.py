from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)

class Message(models.Model):
    value = models.CharField(max_length=10000000)
    data = models.DateTimeField(blank=True)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=200)