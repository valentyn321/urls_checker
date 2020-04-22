from django.views.generic import ListView
from main.models import Url


class UrlListView(ListView):
    model = Url
    template_name = 'main/urls_list.html'
