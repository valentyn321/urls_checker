from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect

from main.models import Url
from main.forms import AddUrlForm

from django.views.decorators.csrf import csrf_exempt
import urllib3


class UrlListView(ListView):
    model = Url
    template_name = 'main/urls_list.html'


@csrf_exempt
def ajax_check(request):
    data = {}
    cleaned_data = []
    for letter in request.POST['checked_ids']:
        if letter.isdigit():
            cleaned_data.append(letter)

    http = urllib3.PoolManager()
    for object_id in cleaned_data:
        obj = Url.objects.get(pk=object_id)
        try:
            if http.request('GET', obj.reference).status == 200:
                obj.usable = True
                obj.checking_now = True
                obj.save()
        except:
            data = {'errors': True}
    return JsonResponse(data)


def add_url(request):
    if request.user.groups.filter(name = "Moderators").exists():
        form = AddUrlForm
        if request.method == "POST":
            form = AddUrlForm(request.POST)
            if form.is_valid():
                url = form.save(commit=False)
                url.save()
            return redirect('main_page')
        else:
            return render(request, "main/url_form.html", {'form': form})
    else:
        return render(request, "main/error_url.html", {})
