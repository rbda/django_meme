from django.urls import path

from .views import HomePageView, CreateBaseImage, CreateMeme, CreateMemeExistingImage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_image/', CreateBaseImage.as_view(), name='add_image'),
    path('add_meme/', CreateMeme.as_view(), name='add_meme'),
    path('add_meme/<int:base_image_pk>', CreateMemeExistingImage.as_view(), name='add_meme_from_image')

]