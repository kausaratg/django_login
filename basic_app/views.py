from django.shortcuts import redirect, render
from basic_app.forms import UserForms, UserProfileForms
from .models import UserProfileModel
from django.contrib.auth.models import User
from django.contrib import messages
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    user_form= UserForms()
    profile_form = UserProfileForms()
    registered = False
    if request.method == 'POST':
    #getting the data from the user
        user_form = UserForms(data=request.POST)
        profile_form = UserProfileForms(data = request.POST)
        # checking if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            #saving only the user_form but not the profile fomr
            user = user_form.save()
            # saving the profile form but not to the database with the use of commit=False
            profile = profile_form.save(commit=False)
            #matching up the user and the profile model
            profile.user = user
            #checking if the user provides image
            if 'profile-pic' in request.FILES:
                #getting the image from the user
                profile.profile_pic = request.FILES['profile_pic']
                #saving the profile
            profile.save()            
            messages.info(request, 'saved')
            registered = True
            login(request, user)
            context = { 'registered':registered}
            return render(request, 'basic_app/registration.html',  context)
        else:
            messages.info(request , 'invalid credentials')
            return redirect('register')
    else:

        context = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}
        return render(request, 'basic_app/registration.html',  context)

def user_login(request):
    username=password=''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('account not active')
        else:
            print('someone tried to login and failed ')
            print(f'{username}, {password}')
            return HttpResponse('invalid supply')
    else:      
        return render(request, 'basic_app/login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

def special_page(request):
    return HttpResponse('special page')