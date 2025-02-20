from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render(request, "index.html")

def paste(request, paste_uid):
    try:
        paste = Paste.objects.get(pk=paste_uid)
        return render(request, 'paste.html', {"paste": paste})
    except Paste.DoesNotExist:
        return render(request, "404.html")


class PasteListView(generic.ListView):
    model = Paste
    template_name = "paste_list.html"

@csrf_exempt
def upload(request):
    if request.method != "POST":
        return render(request, "404.html")
    
    print(request.body)
    try:
        language = request.POST.get("language")
        content  = request.POST.get("content")
        lang     = Language[language]
        print("YEEEE")
        paste = Paste(text=content, language=lang)
        paste.save()
        print(Paste.objects.all())

    except Exception as e:
        print(e)
        return HttpResponse("error occurred")
    
    print("Language: ", request.POST.get("language"))
    return HttpResponse("Done!")
    

"""
    - Add administrator-like routes later
"""