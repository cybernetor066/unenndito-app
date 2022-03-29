import time, bson, json, os, sys, datetime, string, random, ast
from urllib.parse import urlencode

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.core import mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import loader

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger

from .models import UserRegistration, Post
from .forms import UserRegistrationForm

from bson import ObjectId
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import dns

from django.core.serializers import serialize

# Accessing files in directories
if getattr(sys, 'frozen', False):
    # running in a bundled form
    base_dir = sys._MEIPASS # pylint: disable=no-member
else:
    # running normally
    base_dir = os.path.dirname(os.path.abspath(__file__))

# Getting our connection strings, both for mongo and redis and other enviroment variables
load_dotenv()

# connection_string_mongo = os.environ['CONNECTION_STRING_MONGO']













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







# signup view
def signup(request):
    if request.method =='POST':
        form =  UserRegistrationForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            print('HELLO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            useremail = form.cleaned_data['useremail']
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            middlename = form.cleaned_data['middlename']
            lastname = form.cleaned_data['lastname']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            lga = form.cleaned_data['lga']

            # password = form.cleaned_data['password']

            # Confirmations
            print("And selected : '%s' as your username" % useremail)
            print("And: '%s' as your username" % username)
            print("And: '%s' as your firstname" % firstname)
            print("And: '%s' as your middlename" % middlename)
            print("And: '%s' as your lastname" % lastname)
            print("And: '%s' as your home address" % address)
            print("And: '%s' as your phone" % phone)
            print("And: '%s' as your age" % age)
            print("And: '%s' as your lga" % lga)

            # print("And : '%s' as your phone" % password)


            # # # send to our email(Basic email)
            # subject = 'Your Django Test Email(Latest Test)'
            # message = 'Hello Support Goodday! \
            #             This is a Django Test Project Email Test!! \
            #             Here are the user form details entered : \
            #             First name : %s \
            #             Last name : %s \
            #             User Email : %s \
            #             Username : %s And \
            #             Password : %s \
            #             ' % (firstname, lastname, useremail, username, password)
            # from_email = "spacenetngbase@gmail.com"      # Or the admin email address
            # to_email = useremail                        # Or the admin email addres (Same thing here)
            # send_mail(subject, message, from_email, [to_email,], fail_silently=False,)


            # # send to our email(Email with attachment)
            # subject = 'Your Django Test Email(Latest Test)'
            # message = 'Hello Support Goodday! \
            #             This is a Django Test Project Email Test!! \
            #             Here are the user form details entered : \
            #             First name : %s \
            #             Last name : %s \
            #             User Email : %s \
            #             Username : %s And \
            #             Password : %s \
            #             ' % (firstname, lastname, useremail, username, password)
            # from_email = "spacenetngbase@gmail.com"      # Or the admin email address
            # to_email = useremail                        # Or the admin email addres (Same thing here)
            # if subject and message and from_email:
            #     try:
            #         email_msg = EmailMessage(
            #             subject, message, from_email, [to_email,]
            #             )
            #         # img_data = open(file_path, 'rb').read()
            #         # email_msg.attach('your_image.jpg', img_data)
            #         email_msg.attach_file(file_path)
            #         email_msg.send()

            #     except BadHeaderError:
            #         return HttpResponse('Invalid header found.')

            # Then perform database operation
            form.save()

            # confirm operation successfull
            print('User records saved successfully!!!')

            messages.info(request, "Registeration successfull!")


    form = UserRegistrationForm()
    return render(request, 'unenndito_app/signup.html', {"form": form})



# Dashboard view
def dashboard(request):
    return render(request, 'unenndito_app/dashboard.html')



# Blog post list page view
def post_list(request):

    res_object = Post.objects.all()

    context = {
        'post_list': res_object,
    }
    print('All Good!!!')        
    return render(request, 'unenndito_app/post-list.html', context=context)




# Dashboard bills detail page view
# def post_detail(request, bill_id):
def post_detail(request, post_id):    
    context = {
        'post': get_object_or_404(Post, pk=post_id),
    }
        
    return render(request, 'unenndito_app/post-detail.html', context=context)






# error 404 function
def error404(request):
    return render(request, 'unenndito_app/error-404.html')

# error 500 function
def error500(request):
    return render(request, 'unenndito_app/error-500.html')

# maintenance function
def maintenance(request):
    return render(request, 'unenndito_app/maintenance.html')

# faq function
def faq(request):
    return render(request, 'unenndito_app/faq.html')




# def handle_upload_file(file):
#     with open(file_path +file.name,'wb+') as destination:  # Not good to hardcode file paths when programming
#         for chunk in file.chunks():
#             destination.write(chunk)


