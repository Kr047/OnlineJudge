from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_scr(request):
    template = loader.get_template('homescreen.html')
    context = {}
    return HttpResponse(template.render(context,request))