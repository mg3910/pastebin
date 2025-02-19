from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic


# Create your views here.

def index(request):
    return render(request, "index.html")

def paste(request, paste_id):
    try:
        t = Paste.objects.get(pk=paste_id)
        #print(t)
        
        return HttpResponse(t.text)
    except Paste.DoesNotExist:
        return HttpResponse("404!")


class PasteListView(generic.ListView):
    model = Paste
    template_name = "paste_list.html"


def upload(request):
    if request.method != "POST":
        return HttpResponse("404!")
    

"""
    - Add administrator-like routes later
"""