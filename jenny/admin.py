from django.contrib import admin

from .models import BaseImage, FinishedMeme, MemeImage


class FinishedMemeAdmin(admin.ModelAdmin):
    exclude = ('meme_image', )


admin.site.register(BaseImage)
admin.site.register(FinishedMeme, FinishedMemeAdmin)
admin.site.register(MemeImage)
