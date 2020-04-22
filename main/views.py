from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from main.models import Url

from django.views.decorators.csrf import csrf_exempt
import urllib3


class UrlListView(ListView):
    model = Url
    template_name = 'main/urls_list.html'


@csrf_exempt
def ajax_check(request):

    cleaned_data = []
    for letter in request.POST['checked_ids']:
        if letter.isdigit():
            cleaned_data.append(letter)

    http = urllib3.PoolManager()
    for object_id in cleaned_data:
        obj = Url.objects.get(object_id)
        try:
            if http.request('GET', obj.reference).status == 200:
                obj.usable = True
                obj.checking_now = True
                obj.save()
        except:
            return HttpResponse("Something gone bad...")
    return JsonResponse({})
