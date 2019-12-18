from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import BaseImageForm, BaseFinishedMemeForm, MemeCreateCustomForm
from .models import FinishedMeme, BaseImage


class HomePageView(ListView):
    model = FinishedMeme
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['baseimages_list'] = BaseImage.objects.all()
        context['finishedMEMES'] = FinishedMeme.objects.all()
        return context


class CreateBaseImage(CreateView):
    model = BaseImage
    form_class = BaseImageForm
    template_name = 'baseimage.html'
    success_url = reverse_lazy('home')


class CreateMeme(CreateView):
    model = FinishedMeme
    form_class = BaseFinishedMemeForm
    template_name = 'makememe.html'
    success_url = reverse_lazy('home')


class CreateMemeExistingImage(CreateView):
    model = FinishedMeme
    template_name = 'meme_from_image.html'
    fields = None
    form_class = MemeCreateCustomForm
    success_url = reverse_lazy('home')

    def get_initial(self):
        return {
            'base_image': self.kwargs['base_image_pk'],
            'base_image_id': self.kwargs['base_image_pk'],
        }
