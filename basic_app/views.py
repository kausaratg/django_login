from pickle import FALSE
from urllib import request
from django.shortcuts import render

from basic_app.forms import UserForms, UserProfileForms

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(reqeust):
    registered = False
    if request.method == 'POST':
        user_form = UserForms(data=request.POST)
        profile_form = UserProfileForms(data= request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile_user = user_form