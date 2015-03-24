from django.views.generic import ListView
from mixins import *
from base.models import Listing

class HomePageView(LoginRequiredMixin, ListView):
    model = Listing
    template_name = "main/home.html"
    context_object_name = "recent_listings"

    def get_queryset(self, **kwargs):
        queryset = super(HomePageView, self).get_queryset(**kwargs)
        queryset = queryset.order_by('date_created')
        queryset.reverse()
        return queryset[:5]