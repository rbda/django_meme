from django import forms
from django.conf import settings
from jenny.models import BaseImage, FinishedMeme, MemeImage
from jenny.memeGenerator import make_meme
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
        title = cleaned_data.get("title")
        top_string = cleaned_data.get("top_text")
        bottom_string = cleaned_data.get("bottom_text")
        if not bottom_string:
            bottom_string = ""
        if not top_string:
            top_string = ""
        filename = cleaned_data.get("base_image").image
        img = make_meme(top_string=top_string, bottom_string=bottom_string, filename=filename,
                        title=title)
        file_path = "." + settings.MEDIA_URL + "images/memes/" + img.filename
        img.save(file_path, "PNG")
        the_image = Image.open(file_path)
        finished_meme = MemeImage.objects.create(image=the_image.filename)
        cleaned_data['meme_image'] = finished_meme
        return cleaned_data
