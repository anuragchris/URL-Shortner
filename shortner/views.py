from django.shortcuts import redirect, render
import uuid
from .models import Url
from django.http import Http404, HttpResponse, HttpResponseNotFound
# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    try:
        url_details = Url.objects.get(uuid=pk)
    except Url.DoesNotExist:
        raise Http404("URL does not exists")
    return redirect(url_details.link)
