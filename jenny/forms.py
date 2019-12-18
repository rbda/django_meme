from django import forms
from django.conf import settings
from django.utils.text import slugify
from jenny.models import BaseImage, FinishedMeme, MemeImage
from jenny.memeGenerator import *
from PIL import Image


class BaseImageForm(forms.ModelForm):
    class Meta:
        model = BaseImage
        fields = ['image', ]


class BaseFinishedMemeForm(forms.ModelForm):
    class Meta:
        model = FinishedMeme
        fields = ['title', 'top_text', 'bottom_text', 'base_image']


class MemeCreateCustomForm(forms.ModelForm):
    class Meta:
        model = FinishedMeme
        fields = ['title', 'top_text', 'bottom_text', 'base_image', 'meme_image']
        widgets = {
            'base_image': forms.HiddenInput,
            'meme_image': forms.HiddenInput
        }

    def clean(self):
        cleaned_data = super().clean()
        # print(f"cleaned data: {cleaned_data}")
        title = cleaned_data.get("title")
        topString = cleaned_data.get("top_text")
        print(topString)
        bottomString = cleaned_data.get("bottom_text")
        if not bottomString:
            bottomString = ""
        if not topString:
            topString = ""
        filename = cleaned_data.get("base_image").image
        img = make_meme(topString=topString, bottomString=bottomString, filename=filename, title=title)
        file_path = "." + settings.MEDIA_URL + "images/memes/" + img.filename
        img.save(file_path, "PNG")
        the_image = Image.open(file_path)
        finished_meme = MemeImage.objects.create(image=the_image.filename)
        cleaned_data['meme_image'] = finished_meme
        print(f"cleaned data: {cleaned_data}")
        return cleaned_data
