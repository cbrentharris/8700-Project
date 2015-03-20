from django.views.generic import TemplateView
from mixins import *
from base.models import Listing

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "main/home.html"