from django.views.generic import TemplateView
from mixins import *

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "carfinder/home.html"