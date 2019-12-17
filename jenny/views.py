from django.views.generic import ListView
from .models import FinishedMemes, BaseImages


class HomePageView(ListView):
    model = FinishedMemes
    template_name = 'home.html'
