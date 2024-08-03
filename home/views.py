from django.shortcuts import render,redirect
from home.models import problem
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def all_probs(request):
    if request.method == 'GET':

        all_probs = problem.objects.all()

        context = {
            'all_probs':all_probs,
        }

        template = loader.get_template('homescreen.html')
        
        return HttpResponse(template.render(context,request))

def logout_user(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('/auth/login/')