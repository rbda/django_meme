from django.db import models


class FinishedMeme(models.Model):
    title = models.CharField(max_length=250, help_text="a name for your meme")
    top_text = models.CharField(max_length=100, blank=True, null=True, help_text="text at the top of the meme")
    bottom_text = models.CharField(max_length=100, blank=True, null=True, help_text="text at the bottom of the meme")
    base_image = models.ForeignKey('BaseImage', on_delete=models.CASCADE, help_text="image for the meme")
    meme_image = models.ForeignKey('MemeImage', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title


class BaseImage(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.url


class MemeImage(models.Model):
    image = models.ImageField(upload_to='images/memes/')
