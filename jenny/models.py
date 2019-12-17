from django.db import models


class FinishedMemes(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class BaseImages(models.Model):
    image = models.ImageField(upload_to='images/')
