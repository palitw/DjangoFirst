# Create your views here.# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from .models import *

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
#     c = Context({'posts': posts})
    c = t.render({'posts':posts})
    return HttpResponse(c)
    