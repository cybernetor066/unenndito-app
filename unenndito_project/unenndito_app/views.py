from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Accessing files in directories
import sys, os, time
if getattr(sys, 'frozen', False):
    # running in a bundled form
    base_dir = sys._MEIPASS # pylint: disable=no-member
else:
    # running normally
    base_dir = os.path.dirname(os.path.abspath(__file__))



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Or we use a render
def index(request):
    ip = request.META.get('HTTP_X_CLIENT_IP') # Get client IP
    print('Incoming request from IP: ', ip)

    return render(request, 'index.html')


# home view
def home(request):
    return render(request, 'home.html')