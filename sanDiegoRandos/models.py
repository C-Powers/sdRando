from django.db import models

# Create your models here.
class Permanents(models.Model):
    location = models.CharField(max_length=200)
    freeRoute = models.BooleanField()
    distance = models.CharField(max_length=200)
    climb = models.CharField(max_length=200)
    permName = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200)
    permLink = models.URLField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.location
