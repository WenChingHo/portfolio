from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required
def index(request):

    return render(request, 'dashboard/index.html')