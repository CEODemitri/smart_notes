from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    # return HttpResponse('Hello World!')
    # how to render an html; use render function with 3 parameters
    return render(request, 'home/welcome.html', {'today': datetime.today()})


@login_required
def authorized(request):
    return render(request, 'home/authorized.html', {})
# Create your views here.
