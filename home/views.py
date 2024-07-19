from django.shortcuts import render
from home.models import problem
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def all_probs(request):
    all_probs = problem.objects.all()

    context = {
        'all_probs':all_probs,
    }

    template = loader.get_template('homescreen.html')
    
    return HttpResponse(template.render(context,request))